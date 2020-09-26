grep
====

Background info
---------------

Unix grep
.........

The grep filter searches a file for a particular pattern of characters,
and displays all lines that contain that pattern.
The pattern that is searched in the file is referred to as
the regular expression (grep stands for globally search
for regular expression and print out). [1]_

For example ``$ grep README.info`` would print the lines
which have word ``info`` in them:

.. code-block:: shell

  $ grep info README.rst

  Background info
  For example ``$ grep README.info`` would print the contents of this file.
  ...


Task 0
------

``grep`` is a very rich and useful tool. It provides many options to control
its behavior.

1. Run ``man grep`` in shell to see grep's Manual page. Also run ``grep --help`` to see the quick help.
2. Grep ``README.rst`` with the following flags: ``-i`` or ``--ignore-case``; ``-n`` or ``--line-number``;; ``-c`` or ``--count``; ``-v`` or ``--invert-match``.
   For example:

   .. code-block:: shell

     $ grep --line-number info README.rst

     4:Background info
     12:For example ``$ grep README.info`` would print the lines
     ...


Task 1
------

Let's write a tool similar to grep in Python.

The tool ``grep1.py`` should search for an inclusion of a given text in a file.
It should behave similar to UNIX grep: output the lines of the file which
contain the found pattern:

.. code-block:: shell

  $ python grep1.py info README.rst

  Background info
  For example ``$ grep README.info`` would print the contents of this file.
  ...

The tool should also support the following options:

* ``-i``: ignore pattern case, i.e. "INFO", "info" "iNfO" in file all match "info".
* ``-n``: output line numbers in front of matched lines (see example above).
* ``-v``: invert match, i.e. output the lines which do NOT match the pattern.
* ``-c``: output matched lines count instead of the matched lines.

Write the code in ``grep1.py``.
Use ``flake8`` and ``black`` to format your code properly :)


Task 2
------

Unix commands allow grouping short options. For example:

.. code-block::

  $ grep -ni INFO README.rst

  4:Background info
  12:For example ``$ grep README.info`` would print the contents of this file.
  ...

You can imagine, that making the combinations work is such a repetitive task,
that there must be a library for that.
Luckily in Python it is part of the standard library.  available out of the box
`argparse <https://docs.python.org/3/library/argparse.html>`_ - is
a parser for command-line options, arguments and sub-commands.

Your task is to rewrite your Python grep program using ``argparse``. In addition
to supporting the short options, you should also support their long aliases:

* ``-i``, ``--ignore-case``
* ``-n``, ``--line-number``
* ``-c``, ``--count``
* ``-v``, ``--invert-match``

Write the code in ``grep2.py`` file. Remember to validate the code style
with ``flake8`` and auto-format it with ``black`` if needed.

References
----------

.. [1] `grep - GeeksforGeeks <https://www.geeksforgeeks.org/grep-command-in-unixlinux/>`_
