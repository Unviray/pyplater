"""
Helper for Bootstrap 4.3
"""

from pyplate import (
    html,
    head,
    meta,
    body,
    link,
    title as t,
    script,
    div,
    h1,
    blockquote,
    footer,
)
from pyplate.utils import classing


RESPONSIVE_BP = ["xs", "sm", "md", "lg", "xl"]


def starter(*args, **kwargs):
    """
    Starter Template
    """

    BOOTSTRAP_CSS = (
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    )
    INTEGRITY_BSCSS = (
        "sha384-ggOyR0iXCbMQv3Xipma34MD&#43;dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
    )

    POPPER_JS = (
        "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.15.0/umd/popper.min.js"
    )
    INTEGRITY_POJS = (
        "sha384-L2pyEeut/H3mtgCBaUNw7KWzp5n9&#43;4pDQiExs933/5QfaTh8YStYFFkOzSoXjlTb"
    )

    BOOTSTRAP_JS = (
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    )
    INTEGRITY_BSJS = (
        "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM&#43;B07jRM"
    )

    title = kwargs.pop("title", "Document")
    additional_head = kwargs.pop("in_head", [])

    component = html(lang="en")(
        head(
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            link(
                rel="stylesheet",
                href=BOOTSTRAP_CSS,
                integrity=INTEGRITY_BSCSS,
                crossorigin="anonymous",
            ),
            *additional_head,
            t(title),
        ),
        body(
            *args,
            script(src=POPPER_JS, integrity=INTEGRITY_POJS, crossorigin="anonymous"),
            script(src=BOOTSTRAP_JS, integrity=INTEGRITY_BSJS, crossorigin="anonymous"),
        ),
    )

    return component


# Layout


def container(breakpoint="", **kwargs):
    """
    >>> c = container("md")(
    ...     'text'
    ... )
    >>> c.render()
    <div class="container-md">text<div/>
    """

    if breakpoint:
        if breakpoint in RESPONSIVE_BP + ["fluid"]:
            breakpoint = "-" + breakpoint
        else:
            print(f'Breakpoint should be one of {RESPONSIVE_BP} or "fluid')
            breakpoint = ""

    c = kwargs.pop("_class", [])
    c = classing("container" + breakpoint, *c)

    return div(_class=c, **kwargs)


def row(*args, **kwargs):
    """
    >>> c = row('text')
    >>> c.render()
    <div class="row">text<div/>
    """

    c = kwargs.pop("_class", [])
    c = classing("row", *c)

    return div(_class=c, **kwargs)(*args)


def col(breakpoint="", **kwargs):
    """
    >>> c = col("md-6")(
    ...     'text'
    ... )
    >>> c.render()
    <div class="col-md-6">text<div/>
    """

    if breakpoint:
        breakpoint = "-" + breakpoint

    c = kwargs.pop("_class", [])
    c = classing("col" + breakpoint, *c)

    return div(_class=c, **kwargs)


# typography


def display(n=1, **kwargs):
    """
    >>> c = display(3)('text')
    >>> c.render()
    <h1 class="display-3">text<h1/>
    """

    if n < 1 or n > 4:
        print('"n" should be between 1 - 4')

    c = kwargs.pop("_class", [])
    c = classing("display-" + n, *c)

    return h1(_class=c, **kwargs)


def lead(*args, **kwargs):
    """
    >>> c = lead('text')
    >>> c.render()
    <p class="lead">text<p/>
    """

    c = kwargs.pop("_class", [])
    c = classing("lead", *c)

    return div(_class=c, **kwargs)(*args)


def quote(author="", **kwargs):
    class b(blockquote):
        TAG_NAME = "blockquote"

        def __call__(self, *args):
            firstChild = self.content[0](*args)

            return self

    c = kwargs.pop("_class", [])
    c = classing("blockquote", *c)

    return b(_class=c, **kwargs)(
        p(_class="mb-0"), footer(_class="blockquote-footer")(author)
    )


# components


def btn(color="primary", **kwargs):
    tag = kwargs.pop("tag", button)
    outline = kwargs.pop("outline", False)
    size = kwargs.pop("size", "")
    block = kwargs.pop("block", False)

    if tag == a:
        kwargs['role'] = kwargs.pop('role', 'button')
        kwargs['href'] = kwargs.pop('href', '#')
    else:
        kwargs['type'] = kwargs.pop('type', 'button')

    if color:
        if color in COLOR_BP + ["link"]:
            color = "btn-outline-" + color if outline else "btn-" + color
        else:
            print(f'Color should be one of {COLOR_BP} or "link')
            color = ""

    if size:
        if size in ('sm', 'lg'):
            size = "btn-" + size
        else:
            print(f'Size should be one of ["sm", "lg"]')
            size = ""

    if block:
        block = "btn-block"
    else:
        block = ""

    c = kwargs.pop("_class", [])
    c = classing("btn", color, size, block, *c)

    return tag(_class=c, **kwargs)
