from pyplater import Component, button, div


class Button(Component):
    variant = "primary"
    size = None

    def render(self):
        _class = ["btn", f"btn-{self.variant}"]

        if self.size is not None:
            _class.append(f"btn-{self.size}")

        return button(_class=_class)(self.children)


class Card(Component):
    def render(self):
        return div(_class="card")(self.children)

    class Header(Component):
        def render(self):
            return div(_class="card-header")(self.children)

    class Body(Component):
        def render(self):
            return div(_class="card-body")(self.children)

    class Footer(Component):
        def render(self):
            return div(_class="card-footer")(self.children)


def test_button():
    for variant in ["primary", "secondary", "dark", "light"]:
        component = Button("Submit", variant=variant)
        component_lg = Button("Submit", variant=variant, size="lg")

        assert str(component) == (
            f'<button class="btn btn-{variant}">Submit</button>'
        )

        assert str(component_lg) == (
            f'<button class="btn btn-{variant} btn-lg">Submit</button>'
        )


def test_card():
    component = (
        Card(
            Card.Body(
                "Some text within a card body."
            )
        )
    )

    assert str(component) == (
        '<div class="card"><div class="card-body">Some text within a card body.</div></div>'
    )
