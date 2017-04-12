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


| What is the result?
| How can we do a quick test?


Now that we have a string how do we write that string to a file? Or how do we read from a file? Well ...

.. code-block:: c

    FH = open("blah.txt", "w")
    FH.write("Space… the final frontier.")
    FH.close






.. code-block:: c

    with open("blah.txt", "w") as FH:
        FH.write("Space… the final frontier.")
        FH.write(1)



I put an error in the code do you see it? Hint writes only string type. How would we fix this?


