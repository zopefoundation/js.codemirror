.. caution:: 

    This repository has been archived. If you want to work on it please open a ticket in https://github.com/zopefoundation/meta/issues requesting its unarchival.

js.codemirror
*************

Warning
=======

This repository is still work in progress. As the integration of JS-Files in Zope was finally not done with fanstatic, there is currently no initiative for this. If you want to help out, please submit a PR.


Introduction
============

This library packages the javascript library `CodeMirror`_ to be used with `fanstatic`_.

.. _`CodeMirror`: http://codemirror.net/
.. _`fanstatic`: http://fanstatic.org


Update the package
==================

This package contains the whole source code release of `CodeMirror`_ below ``js/codemirror/resources``. To update:

* Download the release from the website or npm. (github is not the release channel of the project and lacks the ``codemirror.js``)

* Extract the release archive to ``js/codemirror/resources``

* Add an entry to changelog and update the version number.
