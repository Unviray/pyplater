from collections import namedtuple

from pyplater.tag import Element
from pyplater import _input, a, button, div, em, h1, html, hr, li, ul


def test_main():
    component = div(h1("Title"), hr(), _class="content", _id="content")

    assert component.render() == (
        '<div class="content" id="content"><h1>Title</h1><hr/></div>'
    )
    assert str(component) == (
        '<div class="content" id="content"><h1>Title</h1><hr/></div>'
    )


def test_param():
    component = a("Google", href="https://www.google.com/")

    assert component.render() == ('<a href="https://www.google.com/">Google</a>')


def test_formating():
    component = h1("My name is {name}")

    assert component.render() == "<h1>My name is </h1>"

    component["name"] = "Alice"
    assert component.render() == "<h1>My name is Alice</h1>"

    component["name"] = "John Doe"
    assert component.render() == "<h1>My name is John Doe</h1>"


def test_formating_attribute():
    component = h1("My name is {person.name} and I'm {person.age} years old")

    Person = namedtuple("Person", ["name", "age"])
    person = Person(name="John Doe", age=28)

    component["person"] = person

    assert component.render() == "<h1>My name is John Doe and I'm 28 years old</h1>"


def test_bind():
    name = "John Doe"
    component = div("My name is {name}").bind(**locals())

    assert component.render() == "<div>My name is John Doe</div>"


def test_recursive_formating():
    component = div("I like these color", ul(li("{spec}"), li("Green"), li("Blue"),))

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
    btn = button("submit", _class=["btn", "btn-primary", "btn-block"])

    assert btn.render() == ('<button class="btn btn-primary btn-block">submit</button>')


def test_children_list():
    component = div([div("A"), div("B")])

    assert component.render() == "<div><div>A</div> <div>B</div></div>"


def test_children_list_recursive():
    component = div([div("A"), div([div("B"), [div("C")]])])

    assert component.render() == "<div><div>A</div> <div><div>B</div> <div>C</div></div></div>"


def test_reserved_name():
    component = _input()

    assert component.render() == "<input/>"


def test_underscore_attribute():
    component = a(data_attribute="value")

    assert component.render() == '<a data-attribute="value"></a>'


def test_call():
    component = div(data="value")(h1('content'), 'text')

    assert component.render() == '<div data="value"><h1>content</h1>text</div>'


def test_custom_tag():
    class an_element(Element):
        TAG_RAW = "{tag_name} [{props} ]"
        TAG_NAME = "Foo"

    component = an_element(data="value")

    assert component.render() == 'Foo [ data="value" ]'


# Each tag


def test_html():
    assert html().render() == "<!doctype html><html></html>"
