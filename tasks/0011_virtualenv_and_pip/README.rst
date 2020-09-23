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

1. Create a virtual environment in this directory.
   Call it ``venv``, so that it can be ignored by git (according to ``.gitignore`` rules in the root of the repository).
2. Activate the virtual environment it.
3. Install ``bottle`` package via ``pip``.
4. Run ``example.py`` - it will start a ``bottle`` http server on port 8080
   Note: ``example.py`` will raise an ``ImportError`` if ``bottle`` package is not found.

5. Open http://localhost:8080/hello/murad in your browser
6. Uninstall ``bottle`` via ``pip``
7. Run ``example.py`` again. Watch an emerging ``ImportError``.
