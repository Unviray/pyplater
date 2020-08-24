from templater import html


def test_html():
    assert html().render() == "<!doctype html><html></html>"
