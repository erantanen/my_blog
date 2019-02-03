raylib basic window with a pause
################################
:date: 2019-01-27 22:28
:author: Ed Rantanen
:category: raylib
:slug: raylib_02
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>




putting in a pause?
...................

How do do we put a pause into the graphics?
The complete pause can be seen here.

  `A pause? <./code_snips/bw_bound_pixel_with_pause.py>`_

The base logic is here.


.. code-block:: c

        if is_key_pressed(KEY_P):
            if pause:
                pause = False
            else:
                pause = True


The first thing we need to have is some sort of check to see if a key is pressed?
And which key we are looking for? These keys can be any combination depending on what
you are trying to accomplish, if we were in landscape moving along a map we might use the the up/left/right (keys)
or we might use a combination of w/a/d instead, and if a shooter type of game maybe the space bar or maybe we
might need a multiplier instead of just walking but shift to run (ie move quicker).
But to keep this initially simple we are just adding a pause.

When looking at the above code we are not making a difference of the case?

 | (lower/upper case)

If you have pulled the code, give it a try with both upper and lower case "p" it will re-act the same.

Before we can use "if pause:" the variable will need to be set outside of the while loop and its done with
" pause = False " This kind of statement gets into the concept of Boolean for further reading look at the link
below.


 | `An in-depth look at python boolean <https://www.codesdope.com/python-boolean/>`_


Now that the check has been accomplised, we can can then move onto using that check with

.. code-block:: c

       # checking if in pause state
        if pause is False:

What this will do is by pass the code block with in the if-statement where everything is drawn/updated.
And the effect of the key press will be?

Now that you have a basic key press, you can go on to try other things with this little bit of code, also
how might we move the draw circle along faster with a key press?

