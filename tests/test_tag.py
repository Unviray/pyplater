from beam import a, button, div, em, h1, hr, li, ul


def test_main():
    component = div(h1("Title"), hr(), _class="content",)

    assert component.render() == (
        '<div class="content"><h1>Title</h1><hr/></div>'
    )


def test_param():
    component = a('Google', href="https://www.google.com/")

    assert component.render() == (
        '<a href="https://www.google.com/">Google</a>'
    )


def test_formating():
    component = h1("My name is {name}")

    assert component.render() == "<h1>My name is </h1>"

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


def test_formating_accessibility():
    li_item = li("{spec}")
    ul_item = ul(li_item, li("Green"), li("Blue"))
    component = div("I like these color", ul_item)

    li_item["spec"] = "Red"
    assert component["spec"] == "Red"


def test_formating_not_found():
    component = div("I like these color")

    assert component["color"] is None


def test_callable_to_str():
    def color():
        return "Red"

    component = div("I like ", color, " color")
    assert component.render() == "<div>I like Red color</div>"


def test_callable_to_tag():
    def color():
        return em("Red")

    component = div("I like ", color, " color")
    assert component.render() == "<div>I like <em>Red</em> color</div>"


def test_class_list():
    btn = button("submit",  _class=["btn", "btn-primary", "btn-block"])

    assert btn.render() == (
        '<button class="btn btn-primary btn-block">submit</button>'
    )
