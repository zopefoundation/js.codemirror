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


codemirror_keymap_emacs = Resource(
    library,
    'keymap/emacs.js',
    depends=[codemirror],
)

codemirror_keymap_sublime = Resource(
    library,
    'keymap/sublime.js',
    depends=[codemirror],
)

codemirror_keymap_vim = Resource(
    library,
    'keymap/vim.js',
    depends=[codemirror],
)
