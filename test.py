from beam import *


titre = h1('Mon nom est: {name}', _class='mb-0')

html = html(
    head(
        meta(charset="utf-{num}")
    ),
    body(titre),
)


titre['name'] = 'Unviray'
html['num'] = 8


print(html.render())