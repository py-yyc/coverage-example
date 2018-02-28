Coverage Example
================

This is a simple project that we can play with to understand some
"coverage" tools in Python. It is essentially the "TicTacToe" program
from a few months ago (it's okay if you didn't come to those meetups).

Setup
-----

Create a virtualenv and install the example::

   virtualenv venv
   ./venv/bin/pip install --editable .
   source ./venv/bin/activate

On Windows, instead of the last line use this::

    ./venv/bin/activate.bat

Running the Tests
-----------------

Once you're set up like the above (in a shell where you've run the
"activate" part) you can run the tests::

    py.test -sv tests

