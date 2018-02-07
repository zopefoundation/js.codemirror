How to use?
===========

To include the basic codemirror javascript and CSS you just need to include a single resource.

You can import ``codemirror`` from ``js.codemirror`` and ``need`` it
where you want these resources to be included on a page::

  >>> from js.codemirror import codemirror
  >>> codemirror.need()

If you want specific bindings to ``vim``, ``emacs`` or ``sublime`` use the ``codemirror_keymap_*`` libraries::

  >>> from js.codemirror import codemirror_keymap_emacs
  >>> from js.codemirror import codemirror_keymap_sublime
  >>> from js.codemirror import codemirror_keymap_vim
  >>> codemirror_keymap_emacs.need()
  >>> codemirror_keymap_sublime.need()
  >>> codemirror_keymap_vim.need()
