PY-Into 4
#########
:date: 2017-04-1 23:34
:author: Ed Rantanen
:category: py-intro
:slug: lesson_4
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>


Loops
.....

Lets start with a for loop, you can think of this as number of revolutions if only one number
is used such as 10, but that static number is very limiting.


.. code-block:: c

    for elm in range(10):
        res = elm * 2
        print(res)



A for loop using a single variable we are moving forward in being dynamic!

.. code-block:: c

    x = 10
    for elm in range(x):
        res = elm * 2
        print(res)




Now we start to get crazy by looping through lists and not just a single variable, the range is set by the size of
the list so we can by pass its use.

.. code-block:: c


    a_group_of_numbers = [ 1,3,7, 9, 12]

    for elm in a_group_of_numbers:
        res = elm * 2
        print(res)





And now an iteration through a dictionary, as we do look at the concatenation and casting

.. code-block:: c

    a_dictionary = {'x': 1, 'y': 2, 'z': 3}

    for key, value in a_dictionary .items():
        value = str(value)
        print(key + " : " + value)







`Moving forward to Lesson 5 <lesson_5.html>`__

`Moving back to Lesson 3 <lesson_3.html>`__