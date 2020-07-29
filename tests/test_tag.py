from beam import div, h1, ul, li


def test_main():
    component = div(h1("Title"), _class="content",)

    assert component.render() == '<div class="content"><h1>Title</h1></div>'


def test_formating():
    component = h1("My name is {name}")

    component["name"] = "Alice"
    assert component.render() == "<h1>My name is Alice</h1>"

    component["name"] = "John Doe"
    assert component.render() == "<h1>My name is John Doe</h1>"


def test_recursive_formating():
    component = div("I like these color",
                    ul(li("{spec}"), li("Green"), li("Blue"),))

    component["spec"] = "Red"
    assert component.render() == (
        "<div>"
        "I like these color"
        "<ul>"
        "<li>Red</li>"
        "<li>Green</li>"
        "<li>Blue</li>"
        "</ul>"
        "</div>"
    )
    component["spec"] = "Purple"
    assert component.render() == (
        "<div>"
        "I like these color"
        "<ul>"
        "<li>Purple</li>"
        "<li>Green</li>"
        "<li>Blue</li>"
        "</ul>"
        "</div>"
    )
