PY-Into 6
#########
:date: 2017-04-1 23:36
:author: Ed Rantanen
:category: py-intro
:slug: lesson_6
:status: published



.. raw:: html

    <embed>
       <br>
    </embed>


Functions
.........

A function, What is it?

It is away to create re-usable code; something you might use more than once or away of
creating blocks of code that are more easily read.

 As an example:
        | A Math function
        | A print statement




From lesson 1 we saw `c = a**2 + b**2` its called Pythagorean Theorem but the original form was very limiting.
How can we make it more usable?

A function can define something with

- no input and no return
- input and no return
- input and a return



.. code-block:: c

    def print_lunchtime():
         print(" Really its lunch time?\n")




.. code-block:: c

    def math_pythag_therem(data):
         print("a good book to read might be " + data)



.. code-block:: c

    def math_pythag_therem(a,b):
         #
         # find the hypotenuse of a right triangle
         #
        result = a**2 + b**2
        c = result**(1/2.0)
        return c



If you want to read up on the Theorem  go to the `Wiki <https://en.wikipedia.org/wiki/Pythagorean_theorem>`_



What ideas can you think of for a print statement? Maybe a template for a repeating form block?
Try to come up with a print function.


.. raw:: html

    <embed>
       <br>
    </embed>



Excel
.....

Now a deep dive.

| Look that example for excel.

 `example:  excel with small functions?   <./code_snips/excel_example.py>`__




.. raw:: html

    <embed>
       <br>
    </embed>




`Moving forward to Lesson 7 <lesson_7.html>`__

`Moving back to Lesson 5 <lesson_5.html>`__

