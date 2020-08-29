"""
pyplater
=========

Build html component with python.

.. codeauthor:: Unviray <unviray@gmail.com>

Usage example:

>>> from pyplater import h1
>>> title = h1("title")
>>> title.render()
<h1>title</h1>
"""


from .tag import (_del, _input, a, abbr, address, article, aside, audio,
                  blockquote, body, br, button, caption, cite, dd, dfn, div,
                  dl, dt, em, fieldset, figcaption, figure, footer, form, h1,
                  h2, h3, h4, h5, h6, head, header, hr, html, i, img, ins, kbd,
                  label, legend, li, link, mark, meta, nav, ol, optgroup,
                  option, p, pre, progress, q, script, section, select, source,
                  span, strong, style, sub, sup, table, tbody, td, textarea,
                  tfoot, th, thead, time, title, tr, ul, video)

__all__ = (
    # Base
    'html', 'head', 'body',

    # Head
    'link', 'meta', 'script', 'style', 'title',

    # Structure
    'abbr', 'blockquote', 'cite', 'q', 'sup', 'sub', 'strong', 'em', 'mark',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'figure', 'figcaption', 'audio',
    'video', 'source', 'a', 'br', 'p', 'hr', 'i', 'address', '_del', 'ins',
    'dfn', 'kbd', 'pre', 'progress', 'time',

    # List
    'ul', 'ol', 'li', 'dl', 'dt', 'dd',

    # Table
    'table', 'caption', 'tr', 'th', 'td', 'thead', 'tbody', 'tfoot',

    # Form
    'form', 'fieldset', 'legend', 'label', '_input', 'button', 'textarea',
    'select', 'option', 'optgroup',

    # Section
    'header', 'nav', 'footer', 'section', 'article', 'aside',

    # Generic
    'div', 'span',
)


__version__ = "2.1.2"
