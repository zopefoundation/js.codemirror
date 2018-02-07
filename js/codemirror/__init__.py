from fanstatic import Library, Resource, Group


library = Library('codemirror', 'resources')


codemirror_js = Resource(
    library,
    'lib/codemirror.js')


codemirror_css = Resource(
    library,
    'lib/codemirror.css')


codemirror = Group([
    codemirror_js,
    codemirror_css,
])
