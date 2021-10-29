"""
pyplater.tags
============

Include all tags.
"""

from .element import Element, SingleElement

# Base


class html(Element):
    TAG_RAW = "<!doctype html><{tag_name}{props}>{children}</{tag_name}>"


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


# HTML5

class details(Element):
    pass

class summary(Element):
    pass

class dialog(Element):
    pass

class menu(Element):
    pass

class command(Element):
    pass

class datalist(Element):
    pass

class output(Element):
    pass

class meter(Element):
    pass

class wbr(SingleElement):
    pass

class hgroup(Element):
    pass

class keygen(Element):
    pass
