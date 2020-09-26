Python Virtual Environment
==========================

Background info
---------------

virtualenv
..........

``virtualenv`` is a tool to create isolated Python environments.

Imagine that you are writing a program which depends on a library ``LibFoo`` version 2.
However there is another program, which depends on older version of ``LibFoo`` - version 1.
How could you put both programs in your system without ruining the dependencies?
Virtualenv to rescue!

Further study:

* https://realpython.com/python-virtual-environments-a-primer/
* https://virtualenv.pypa.io/en/latest/
* https://www.youtube.com/watch?v=N5vscPTWKOk


pip
...

``pip`` is a Python packages installation and management tool.

Pip can be used to install packages in activated (isolated) virtual environment,
or system-wide.

Further study:

* https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
* https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/


Task
----

The enclosed ``example.py`` is a simple program which starts a local
HTTP server and returns a HTTP response on ``/hello/{name}`` endpoint.
It requires `Bottle <https://bottlepy.org/docs/dev/>`_ to run.
**Bottle** is a fast, simple and lightweight WSGI micro web-framework for Python.
However Bottle is not a part of Python standard library.

Steps
.....

1. Create a virtual environment in this directory.
   Call it ``.env``, so that it can be ignored by git
   according to ``.gitignore`` rules in the root of the repository.
2. Activate the virtual environment it.
3. Install ``bottle`` package via ``pip``.
4. Run ``example.py`` - it will start a ``bottle`` HTTP server on port 8080
5. Open http://localhost:8080/hello/murad in your browser.
   - What does the page say?
6. Uninstall ``bottle`` via ``pip``
7. Run ``example.py`` again.
   - Watch an emerging ``ImportError``.
