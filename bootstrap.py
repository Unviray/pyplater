from templater import button, div
from templater.utils import classing


def container(*args, breakpoint=''):
    if breakpoint:
        breakpoint = '-' + breakpoint

    return div(*args, _class=f"container{breakpoint}")


def alert(*args):
    return div(*args, _class=["alert", "alert-primary"], role="alert")


def btn(*args, color="primary", block=False, **kwargs):
    _class = kwargs.pop('_class', [])

    c = ["btn", f"btn-{color}"]

    if block:
        c.append("btn-block")

    c = classing(_class, c)

    return button(*args, _class=c, **kwargs)

container()
