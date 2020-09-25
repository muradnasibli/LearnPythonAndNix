PEP 8
=====

Background info
---------------

PEPs
....

**PEP** stands for **Python Enhancement Proposal**.
A PEP is a design document providing information to the Python community,
or describing a new feature for Python or its processes or environment.
The PEP should provide a concise technical specification of the feature
and a rationale for the feature.

PEP 8
.....

`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_
defines style guide for python code.

For example, the following code has style violations according
to PEP 8:

.. code-block:: python

   def CalculateVelocity(deltaX, t):
       velocity = deltaX/t

* ``CalculateVelocity`` - *Function name should be lowercase*
* ``deltaX`` - *argument name should be lowercase*
* ``deltaX/t`` - *no spacing between operators*


Tools
.....

Python ecosystem has an army of tools to detect formatting
errors and re-format existing code.
My favourites are:

* `flake8 <https://flake8.pycqa.org/en/latest/>`_ - a tool for style guide enforcement.
* `black <https://github.com/psf/black>`_ - the uncompromising Python code formatter.


Task
----

Create a virtual environment in the task directory and activate it.
Install ``flake8``, ``pep8-naming`` (flake8 plugin to verify naming conventions)
and ``black``.

1. Run ``flake8`` to inspect ``bad_formatted_example.py``:

   .. code-block:: shell

      $ flake8 bad_formatted_example.py

   What are the errors reported by flake8?

2. Run ``black`` to reformat the code. First run it with ``--diff`` option:

   .. code-block:: shell

      $ black --diff bad_formatted_example.py


   Does black report any formatting changes?
   Run black without ``--diff``. It should now reformat the file.
   Notice that black did not fix all style guide issues.


3. Update the code according to PEP 8 guidelines and run flake8 again.
   There should be no errors left :)
