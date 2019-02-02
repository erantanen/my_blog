PY-Into 5
#########
:date: 2017-04-1 22:35
:author: Ed Rantanen
:category: py-intro
:slug: lesson_5
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>




getopt
......

getopt is a library for utilizing command line options. By adding arguments we can extend simple static variables.

As we have worked with Pythagorean expression, all the variables have been static in nature now with we can make a
utility that that will take any combination of numbers.



`simple get opt example <./code_snips/getopt_test.py>`__


Using the example code make a program that you can run from the command line, and test it.



.. raw:: html

    <embed>
       <br>
    </embed>



fizzbuzz?
.........

We are going to use the fizzbuzz as an entry point for the first Euler problem.


   | If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
   | The sum of these multiples is 23.
   | Find the sum of all the multiples of 3 or 5 below 1000.


`Project Euler site <https://projecteuler.net/problem=1>`__

Going back to the modulo examples, we now add these to an if statement.



.. code-block:: c

   elm = 10

    if elm%3 == 0:
        print("elm has no remainder")



Right this is pretty straight forward, maybe? Now lets replace elm's static number with
for loop and cycle through some numbers


.. code-block:: c

   for elm in range(100):
        if elm%3 == 0:
             print("elm has no remainder")


This loop will print all mod 3 results, but the question is geared toward multple 3 and 5.


.. code-block:: c

   for elm in range(100):
        if elm%3 == 0 and elm%5 == 0;
             print("elm has no remainder")

With a compound conditional we can begin to see how you might solve the whole fizzbuzz issue.

As an example of the same algorithm being used across different
languages look at `my fizzbuzz page <http://pseudopoint.net/the-buzz-of-fizz-code.html>`__

Also if you want to fork my code or add to it on `GitHub <https://github.com/erantanen/fizzbuzz>`__ go forth
and do great things







.. raw:: html

    <embed>
       <br>
    </embed>






`Moving forward to Lesson 6 <lesson_6.html>`__

`Moving back to Lesson 4 <lesson_4.html>`__





