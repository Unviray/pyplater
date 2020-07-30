# Beam

Build `html` component with python.

```python
from beam import *  # import all tag


documents = html(
    head(
        meta(charset="utf-8"),
        link(rel="stylesheet", href="./style.css"),
        title("Documents"),
    ),
    body(
        h1("The title"),
        p("lorem ipsum"),
    ),
)


print(documents.render())
```