from pyplater.utils import Attrs, classing


def test_classing():
    data = ['fff', 'sss ee', ['aa', 'ww', ('az', 's', 'at'), 'un']]

    result = classing(data)
    assert result == 'fff sss ee aa ww az s at un'

    result = classing(*data)
    assert result == 'fff sss ee aa ww az s at un'


def test_attrs():
    attrs = Attrs({"id": "important", "href": "https://google.com"})

    assert attrs["id"] == "important"
    assert attrs.href == "https://google.com"
