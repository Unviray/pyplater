"""
pyplater.element
============

Include definitions of Element and SingleElement.
"""

from typing import List

from .utils import Attrs, classing


class Element(object):
    """
    Base element of any tags.
    """

    TAG_RAW = "<{tag_name}{attrs}>{children}</{tag_name}>"
    # TAG_RAW = "<Element class='bg-dark'>The element</Element>"

    TAG_NAME = None

    def __init__(self, *children, **attrs):
        self._class = attrs.pop("_class", [])
        if isinstance(self._class, str):
            self._class = self._class.split(" ")

        self.attrs = Attrs(attrs)
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

            if isinstance(child, Element):
                child = child.render()
            elif isinstance(child, (list, tuple)):
                child = " ".join(self._render_children(child))
            # elif isinstance(child, str):
            else:
                child = str(child)

            result.append(self._formatting(child))

        return result

    def render(self) -> str:
        """
        Transform Element to str and recursively their children.
        """

        attrs = []  # handle list of attrs ex: href="https://github.com"

        if len(self._class) != 0:
            value_class = classing(self._class)
            attrs.append(f'class="{value_class}"')

        # render attribute
        for key in self.attrs:
            # ex: href="https://{site}"
            if key.startswith("_"):
                key_attrs = key.replace("_", "", 1)  # _class -> class
            else:
                key_attrs = key.replace("_", "-")  # aria_clic -> aria-click
            value_attrs = self.attrs[key]

            if value_attrs == True:
                result = key_attrs  # uni-attribute. ex: disable
            elif value_attrs == False:
                pass
            else:
                result = f'{key_attrs}="{value_attrs}"'
                # ex: href="https://www.google.com"

            attrs.append(self._formatting(result))

        # add space between tag_name and attrs
        if len(attrs) == 0:
            first_space = ""
        else:
            first_space = " "

        return self.TAG_RAW.format(
            tag_name=self.TAG_NAME,
            attrs=first_space + " ".join(attrs),
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
        return self.render()

    def __set_parent(self, parent):
        self.parent = parent


class SingleElement(Element):
    """
    For single tag like: <img/>, <hr/> ...
    """

    TAG_RAW = "<{tag_name}{attrs}/>"

    def __init__(self, *children, **attrs):
        # Convert children to attrs
        attrs["children"] = attrs.get("children", [])
        attrs["children"].extend(children)

        if len(attrs["children"]) == 0:
            del attrs["children"]

        super(SingleElement, self).__init__(**attrs)
