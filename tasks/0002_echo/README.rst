echo
====

Background info
---------------

Unix echo
.........

``echo`` is a fundamental command found in most operating systems that offer a command line. It displays a line of text passed to it. For example:

.. code-block:: shell

  $ echo This works!
  This works!

Echo is frequently used in scripts, batch files, and as part of individual commands; anywhere you may need to insert text. Many command shells such as bash, ksh and csh implement echo as a built-in command [1]_.

Command-line arguments
......................

A command-line argument or parameter is an item of information provided to a program when it is started. A program can have many command-line arguments that identify sources or destinations of information, or that alter the operation of the program.

When a command processor is active a program is typically invoked by typing its name followed by command-line arguments (if any). For example, in Unix and Unix-like environments, an example of a command-line argument is:

.. code-block:: shell

  $ rm file.s

``"file.s"`` is a command-line argument which tells the program ``rm`` to remove the file ``"file.s"``.


Task
----

Write a simple ``echo`` program in Python. It should print the text passed to it.
For example:

.. code-block:: shell

  $ python echo.py This works!
  This works!


**Hints:**

* Use ``sys.argv`` list to access command-line arguments.


References
----------

.. [1] `echo - TutorialsPoint <https://www.tutorialspoint.com/unix_commands/echo.htm>`_
.. [2] `Command-line interface, Wikipedia <https://en.wikipedia.org/wiki/Command-line_interface#Arguments>`_
