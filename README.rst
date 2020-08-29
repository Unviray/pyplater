Pyplaterr
=========

Build ``html`` component with python.

.. code-block:: python

    from pyplater import *  # import all tag

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


Contributing
------------

Whether reporting bugs, discussing improvements and new ideas or writing
extensions: Contributions to Pyplaterr are welcome! Here's how to get started:

1. Check for open issues or open a fresh issue to start a discussion around
   a feature idea or a bug
2. Fork `the repository <https://github.com/Unviray/pyplater/>`_ on Github,
   create a new branch off the `master` branch and start making your changes
   (known as `GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_)
3. Write a test which shows that the bug was fixed or that the feature works
   as expected to cover your change
4. Send a pull request and bug the maintainer until it gets merged and
   published ☺
