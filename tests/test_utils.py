from pyplater.utils import Props, classing


def test_classing():
    data = ['fff', 'sss ee', ['aa', 'ww', ('az', 's', 'at'), 'un']]

    result = classing(data)
    assert result == 'fff sss ee aa ww az s at un'

    result = classing(*data)
    assert result == 'fff sss ee aa ww az s at un'


def test_props():
    props = Props({"id": "important", "href": "https://google.com"})

    assert props["id"] == "important"
    assert props.href == "https://google.com"
