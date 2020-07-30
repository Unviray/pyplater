"""
beam.tag.

Include all tags.
"""


class Element(object):
    """Base element of any tags."""

    TAG_RAW = "<{tag_name} {params}>{contents}</{tag_name}>"
    # TAG_RAW = "<Element class='bg-dark'>The element</Element>"

    def __init__(self, *args, **kwargs):
        self.param = kwargs
        self.content = list(args)
        self.formated = {}

    def render(self):
        params = []
        contents = []

        for key in self.param:
            # ex: class="bg-{color}"
            result = f'{key.replace("_", "")}="{self.param[key]}"'
            # ex: class="bg-dark"
            params.append(self.formating(result))

        for content in self.content:
            if callable(content):
                content = content()

            if isinstance(content, Element):
                result = content.render()
            # elif isinstance(content, str):
            else:
                result = str(content)
            contents.append(self.formating(result))

        if len(params) == 0:
            tag_raw = self.TAG_RAW.replace(" ", "")
        else:
            tag_raw = self.TAG_RAW

        return tag_raw.format(
            tag_name=self.__class__.__name__,
            params=" ".join(params),
            contents="".join(contents),
        )

    def formating(self, text):
        key = self.formated.copy()
        while True:
            try:
                return text.format_map(key)
            except KeyError as k:
                key[str(k).replace("'", "")] = ""

    def __setitem__(self, key, value):
        """
        Set item used on formating
        """
        self.formated[key] = value

        for content in self.content:
            if isinstance(content, Element):
                content[key] = value

    def __getitem__(self, key):
        try:
            return self.formated[key]
        except KeyError:
            for content in self.content:
                if isinstance(content, Element):
                    if content[key] is not None:
                        return content[key]

            return None


class SingleElement(Element):
    TAG_RAW = "<{tag_name} {params} />"

    def __init__(self, **kwargs):
        super(SingleElement, self).__init__(**kwargs)


# Base


class html(Element):
    pass


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
