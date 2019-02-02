raylib intro
############
:date: 2019-01-27 22:30
:author: Ed Rantanen
:category: raylib
:slug: raylib_intro
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>




an intro
...............

raylib what is it?
Its a raw graphics lib!

| it's open source
| it can be used with variety of languages
| it can be ran on variety of platforms

| It has some crazy examples already built at the main site  `raylib <https://www.raylib.com//>`_
|

| but what I am going to be looking at is a python version `raylib-py <https://github.com/overdev/raylib-py>`_

First step would be to "pip" the package, if you look at the raylib python page hit has a some directions
for installation. At this point we are not worried about python v2 or v3 so pull what ever your python
currently have installed.

.. code-block:: c

       from raylibpy import *
    ImportError: No module named 'raylibpy'


| If you are having problems with not finding raylibpy after pip'ng,
| check your site packages, you might have say 3.5 and 3.7 installed
| and both can have site packages.




Once that is done.


Okay lets jump right in to some code, we will step through the first example.

The first example we have is  `a basic window that prints a string of text <./code_snips/basic_window.py>`_

How do we start

.. code-block:: c

       from raylibpy import *

with this line we have pulled in the raylib package/library

the next thing we will need to do is initiate a window, I have added a few vars to the
line but later it will make sense why we might not want to hard code these, also within
the init window, this is where you set the title to the window.

.. code-block:: c

    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "the moving fox?")


Just like video we can set the frames per second right now they are set to 60, this
be adjusted up or down depending on what you are doing.

.. code-block:: c

    set_target_fps(60)


Now building the contents of the window. There are two lines begin/end drawing.
All the window building is taking place between these two lines.
The clear background comes into play with the fps setting this is gets reset with every
frame.


.. code-block:: c

   while not window_should_close():

        begin_drawing()
        clear_background(BLACK)
        draw_text(data, screen_width_center, screen_height_center, 15, GREEN)

        end_drawing()

    close_window()



Run the code from the example and see how it works, change settings to see a result
break it and then fix it.






