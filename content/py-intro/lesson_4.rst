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


for loops
.........

Lets start with a "for" loop, you can think of this as number of revolutions; if only one number
is used such as 10 as a static number it is very limiting.


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

    for key, value in a_dictionary.items():
        value = str(value)
        print(key + " : " + value)





while loops
...........

A while loop will continue to cycle as long as its conditional statement is true. These statements can be hazard to
your health, unlike a for loop that has a beginnings and an end, the while loop just goes and goes and goes.


.. code-block:: c

    while x < 10:
        print(x)
        x =+ 1



Run the above code, what is the result?

  | What is the fix for the above code?
  | What is the condition being set? or not set?



Here is a some real/sudo code, but the idea is for an example of socket listener for a web site with the idea
of continuous running while loop.

.. code-block:: c

       try:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       except socket.error:
          print 'Failed to create socket'
          sys.exit()
       s.bind(host,port)
       s.listen(5)
       conn_good = 0
       while(conn_godd == 0):
           if client.recv() >= 4096:
               conn_good = 1
           elif client.timeout == "extreme":
                conn_good = 1
           else:
             print("keep running")




.. raw:: html

    <embed>
       <br>
    </embed>




`Moving forward to Lesson 5 <lesson_5.html>`__

`Moving back to Lesson 3 <lesson_3.html>`__