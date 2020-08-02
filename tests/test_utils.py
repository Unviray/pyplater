from beam.utils import classing


def test_classing():
    data = ['fff', 'sss ee', ['aa', 'ww', ('az', 's', 'at'), 'un']]

    result = classing(data)
    assert result == 'fff sss ee aa ww az s at un'

    result = classing(*data)
    assert result == 'fff sss ee aa ww az s at un'
