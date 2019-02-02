raylib basic window with item moving
####################################
:date: 2019-01-27 22:29
:author: Ed Rantanen
:category: raylib
:slug: raylib_01
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>




something moving?
.................

Okay the intro (previous post) only had static text which is kind of boring, necessary at times but boring.


  `A basic window that moves a pixel? <./code_snips/bw_mov_pixel.py>`_

Well its really not just a pixel, it would be to small for our example, so we are going to use a very very small
circle.

.. code-block:: c

        current_y = screen_height - shifter_y
        draw_circle(current_x, current_y, 2, GREEN)
        print(current_y)
        shifter_y += 1

As you can see we have set up some variables to help our circle of size 2 move along the y axis, something to note
which will help later is the print statement. Printing out our current position of y you will be able to see
the number slowly decrementing but then it goes into negative numbers.

 | The size of the screen height it is 450 pixels.


And as the math goes, you have to mentally shift where y starts, the window = 800x450 (x:y) with 0:0 starting in the upper
left corner. So if we want our dot to start at the bottom then move to the top,
we will have to decrement against the screen height.

As this circle moves upwards and out of the bound of the window, it will continue till we force a check of window
bounds.

  `A simple location check for circle? <./code_snips/bw_bound_pixel.py>`_

.. code-block:: c

       if current_y == 0:
            msg_1 = 'The circle has reached the top of the screen'
            draw_text(msg_1, 20, screen_height-20, 20, WHITE)


Now the program wont continue into "Infinity and beyond" as Buzz Lightyear might say.

With this simple check we could do several things now, make the circle appear to bounce?

 | Or do some other gymnastics maneuver.
 | Or we might need to add a pause to the the window?


