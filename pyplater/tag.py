"""
pyplater.tag
============

Include all tags.
"""

from typing import List

from .utils import Props, classing


class Element(object):
    """
    Base element of any tags.
    """

    TAG_RAW = "<{tag_name}{props}>{childrens}</{tag_name}>"
    # TAG_RAW = "<Element class='bg-dark'>The element</Element>"

    TAG_NAME = None

    def __init__(self, *children, **props):
        self._class = props.pop("_class", [])
        if isinstance(self._class, str):
            self._class = self._class.split(" ")

        self.props = Props(props)
        self.children = list(children)
        self.formated = {}

        self.parent = None

        for children in self.children:
            if isinstance(children, Element):
                children.__set_parent(self)

        self.TAG_NAME = (
            self.TAG_NAME or self.__class__.__name__.replace("_", "")
        )

    def _render_children(self, childrens=None) -> List[str]:
        result = []

        if childrens is None:
            childrens = self.children

        for children in childrens:
            if callable(children):
                children = children()

            if isinstance(children, Element):
                children = children.render()
            elif isinstance(children, (list, tuple)):
                children = " ".join(self._render_children(children))
            # elif isinstance(children, str):
            else:
                children = str(children)

            result.append(self._formating(children))

        return result

    def render(self) -> str:
        """
        Transform Element to str and recursively their children.
        """

        props = []  # handle list of props ex: href="https://github.com"
        childrens = []  # handle list of childrens ex: <p>name</p>

        if len(self._class) != 0:
            value_class = classing(self._class)
            props.append(f'class="{value_class}"')

        # render attribute
        for key in self.props:
            # ex: href="https://{site}"
            if key.startswith("_"):
                key_props = key.replace("_", "", 1)  # _class -> class
            else:
                key_props = key.replace("_", "-")  # aria_clic -> aria-click
            value_props = self.props[key]

            if value_props == True:
                result = key_props  # uni-attribute. ex: disable
            elif value_props == False:
                pass
            else:
                result = f'{key_props}="{value_props}"'
                # ex: href="https://www.google.com"

            props.append(self._formating(result))

        # render children
        childrens = self._render_children()

        # add space between tag_name and props
        if len(props) == 0:
            first_space = ""
        else:
            first_space = " "

        return self.TAG_RAW.format(
            tag_name=self.TAG_NAME,
            props=first_space + " ".join(props),
            childrens="".join(childrens),
        )

    def _formating(self, text) -> str:
        """
        Get setted item and format :param text:
        """

        formating_map = {}
        for key in self.formated:
            formating_map[key] = self.formated[key]

        unknown_key = None
        while True:
            try:
                return text.format_map(formating_map)
            except KeyError as k:
                formating_map[str(k).replace("'", "")] = ""
                unknown_key = str(k)
            except AttributeError:
                raise AttributeError(f"Unknown variable {unknown_key}")

    def bind(_self, **kwargs):
        for key in kwargs:
            _self[key] = kwargs[key]

        return _self

    def __setitem__(self, key, value):
        """
        Set item used on _formating.
        """

        self.formated[key] = value

        for children in self.children:
            if isinstance(children, Element):
                children[key] = value

    def __getitem__(self, key):
        """
        Get setted item and recursively in self.children
        """

        try:
            return self.formated[key]
        except KeyError:
            for children in self.children:
                if isinstance(children, Element):
                    if children[key] is not None:
                        return children[key]

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

    TAG_RAW = "<{tag_name}{props}/>"

    def __init__(self, *children, **props):
        # Convert children to props
        props["children"] = props.get("children", [])
        props["children"].extend(children)

        if len(props["children"]) == 0:
            del props["children"]

        super(SingleElement, self).__init__(**props)


# Base


class html(Element):
    TAG_RAW = "<!doctype html><{tag_name}{props}>{childrens}</{tag_name}>"


class head(Element):
    pass


class body(Element):
    pass


# Head


class link(SingleElement):
    pass


class meta(SingleElement):
    pass


class script(Element):
    pass


class style(Element):
    pass


class title(Element):
    pass


# Structure


class abbr(Element):
    pass


class blockquote(Element):
    pass


class cite(Element):
    pass


class q(Element):
    pass


class sup(Element):
    pass


class sub(Element):
    pass


class strong(Element):
    pass


class em(Element):
    pass


class mark(Element):
    pass


class h1(Element):
    pass


class h2(Element):
    pass


class h3(Element):
    pass


class h4(Element):
    pass


class h5(Element):
    pass


class h6(Element):
    pass


class img(SingleElement):
    pass


class figure(Element):
    pass


class figcaption(Element):
    pass


class audio(Element):
    pass


class video(Element):
    pass


class source(Element):
    pass


class a(Element):
    pass


class br(SingleElement):
    pass


class p(Element):
    pass


class hr(SingleElement):
    pass


class i(Element):
    pass


class address(Element):
    pass


class _del(Element):
    pass


class ins(Element):
    pass


class dfn(Element):
    pass


class kbd(Element):
    pass


class pre(Element):
    pass


class progress(Element):
    pass


class time(Element):
    pass


# List


class ul(Element):
    pass


class ol(Element):
    pass


class li(Element):
    pass


class dl(Element):
    pass


class dt(Element):
    pass


class dd(Element):
    pass


# Table


class table(Element):
    pass


class caption(Element):
    pass


class tr(Element):
    pass


class th(Element):
    pass


class td(Element):
    pass


class thead(Element):
    pass


class tbody(Element):
    pass


class tfoot(Element):
    pass


# Form


class form(Element):
    pass


class fieldset(Element):
    pass


class legend(Element):
    pass


class label(Element):
    pass


class _input(SingleElement):
    pass


class button(Element):
    pass


class textarea(Element):
    pass


class select(Element):
    pass


class option(Element):
    pass


class optgroup(Element):
    pass


# Section


class header(Element):
    pass


class nav(Element):
    pass


class footer(Element):
    pass


class section(Element):
    pass


class article(Element):
    pass


class aside(Element):
    pass


# Generic


class div(Element):
    pass


class span(Element):
    pass
