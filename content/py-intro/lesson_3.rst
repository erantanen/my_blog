PY-Into 3
#########
:date: 2017-04-1 23:33
:author: Ed Rantanen
:category: py-intro
:slug: lesson_3
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>


strings
.......


Python has some really interesting tools to work with strings
    *strings*  are groups of letters and/or numbers

.. code-block:: c

    blah = "Beam Me Up, Scotty"
    blah[::-1]

| The -1 syntax is quite interesting, try it in the python shell.
| What is the result?
| Doing a quick test what other variations can you see?

- "\n" when working with strings sometimes you might want a new line
- "\t" or maybe a tab.

The "\\" is called an escape character. What other escape sequences are there?




=====

Now that we have a string how do we write that string to a file? Or how do we read from a file? Well ...

.. code-block:: c

    FH = open("blah.txt", "w")
    FH.write("Space… the final frontier.")
    FH.close


A different way to open a file, this one does not require a close.


.. code-block:: c

    with open("blah.txt", "w") as FH:
        FH.write("Space… the final frontier.")
        FH.write(1)



| I put an error in the code do you see it?
| Hint "write" only utilizes string type unless its called out.
| How would we fix this?

 `example: a quick fix?  <./code_snips/file_open.py>`__

Now reading and appending are similar to writing, but we change out the "w" with an "r" or "a" now if we want to
read something it will have to be captured by a variable.

.. code-block:: c

    FH = open("blah.txt", "r")
    file_input = FH.read()
    FH.close


Once we have the variable file_input with some data what should we do with it now?

| Test this out with the python shell!