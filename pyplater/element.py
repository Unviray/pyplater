"""
pyplater.element
================

Include definitions of Element and SingleElement.
"""

import warnings
from typing import List

from .utils import Props, classing


class Element(object):
    """
    Base element of any tags.
    """

    TAG_RAW = "<{tag_name}{props}>{children}</{tag_name}>"
    # TAG_RAW = "<Element class='bg-dark'>The element</Element>"

    TAG_NAME = None

    def __init__(self, *children, **props):
        self._class = props.pop("_class", [])
        if isinstance(self._class, str):
            self._class = self._class.split(" ")

        self.props = Props(props)
        self.children = list(children)
        self.formatted = {}

        self.parent = None

        for child in self.children:
            if isinstance(child, Element):
                child.__set_parent(self)

        self.TAG_NAME = (
            self.TAG_NAME or self.__class__.__name__.replace("_", "")
        )

    def _render_children(self, children=None) -> List[str]:
        result = []

        if children is None:
            children = self.children

        for child in children:
            if callable(child):
                child = child()

            elif isinstance(child, (list, tuple)):
                child = " ".join(self._render_children(child))

            elif isinstance(child, str):
                child = str(child)

            while isinstance(child, Element):
                child = child._render()

            result.append(self._formatting(child))

        return result

    def _render(self) -> str:
        """
        Transform Element to str and recursively their children.
        """

        props = []  # handle list of props ex: href="https://github.com"

        if len(self._class) != 0:
            value_class = classing(self._class)
            props.append(f'class="{value_class}"')

        # render attribute
        for key in self.props:
            if key == 'children':
                warnings.warn(f"Warning: a child is passed to the SingleElement {self.TAG_NAME}")
                continue

            # ex: href="https://{site}"
            if key.startswith("_"):
                key_props = key.replace("_", "", 1)  # _class -> class
            else:
                key_props = key.replace("_", "-")  # aria_clic -> aria-click
            value_props = self.props[key]

            if value_props is True:
                result = key_props  # uni-attribute. ex: disable
            elif value_props is False:
                result = ""
            else:
                result = f'{key_props}="{value_props}"'
                # ex: href="https://www.google.com"

            props.append(self._formatting(result))

        # add space between tag_name and props
        if (len(props) == 0) or (props == [""]):
            first_space = ""
        else:
            first_space = " "

        return self.TAG_RAW.format(
            tag_name=self.TAG_NAME,
            props=first_space + " ".join(props),
            children="".join(self._render_children()),
        )

    def _formatting(self, text) -> str:
        """
        Get setted item and format :param text:
        """

        formatting_map = {}
        for key in self.formatted:
            formatting_map[key] = self.formatted[key]

        unknown_key = None
        while True:
            try:
                return text.format_map(formatting_map)
            except KeyError as k:
                formatting_map[str(k).replace("'", "")] = ""
                unknown_key = str(k)
            except AttributeError:
                raise AttributeError(f"Unknown variable {unknown_key}")

    def bind(_self, **kwargs):
        for key in kwargs:
            _self[key] = kwargs[key]

        return _self

    def __setitem__(self, key, value):
        """
        Set item used on _formatting.
        """

        self.formatted[key] = value

        for child in self.children:
            if isinstance(child, Element):
                child[key] = value

    def __getitem__(self, key):
        """
        Get setted item and recursively in self.children
        """

        try:
            return self.formatted[key]
        except KeyError:
            for child in self.children:
                if isinstance(child, Element):
                    if child[key] is not None:
                        return child[key]

            return None

    def __call__(self, *children):
        """
        Populate children
        """

        self.children.extend(children)

        return self

    def __str__(self) -> str:
        return self._render()

    def __set_parent(self, parent):
        self.parent = parent


class SingleElement(Element):
    """
    For single tag like: <img/>, <hr/> ...
    """

    TAG_RAW = "<{tag_name}{props}/>"

    def __init__(self, *children, **props):
        # Convert children to props
        props["children"] = props.get("children", [])
        props["children"].extend(children)

        if len(props["children"]) == 0:
            del props["children"]

        super().__init__(**props)
