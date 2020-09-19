cat
===

Background info
---------------

Unix cat
........

Cat command concatenate FILE(s), or standard input, to standard output.
With no FILE, or when FILE is -, it reads standard input. [1]_

For example ``$ cat README.rst`` would print the contents of this file.


Task
----

Write a simple ``cat`` program in Python. It should print the contents
of file passed to it by path.

For example:

.. code-block:: shell

  $ python cat.py README.rst
  cat
  ===

  ...
  ...


**Hints:**

* Use ``sys.argv`` to get input file path
* See https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files for
  details on reading files in Python
* Remember to print a human-friendly message when no file path is
  passed to ``cat.py``.


References
----------

.. [1] `cat - TutorialsPoint <https://www.tutorialspoint.com/unix_commands/cat.htm>`_

