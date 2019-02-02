PY-Into 7
#########
:date: 2017-04-1 22:33
:author: Ed Rantanen
:category: py-intro
:slug: lesson_7
:status: published


.. raw:: html

    <embed>
       <br>
    </embed>


newspaper
.........

newspaper is library that we will use to pull data from media sites. Follow the link, read and try the intro examples.


`newspaper <https://github.com/codelucas/newspaper>`__

With this library we will be pulling the data in to a variable for parsing (searching) that will later be analyzed
for some criteria.


Now that you have experimented with news paper, build a function that calls it and has an output.


.. raw:: html

    <embed>
       <br>
    </embed>



google finance
..............

  | How to capture real time stock data?
  | We can use an API (application program interface) that Google created to do pulls.


`google finance at github <https://github.com/hongtaocai/googlefinance>`__



.. code-block:: c

    from googlefinance import getQuotes
    import json

    print(json.dumps(getQuotes('AAPL'), indent=2))


Lets try the above code out in pycharm.


 | This code is very simple, and static but by using the elements that we have learned so far:

  - function creation
  - looping
  - list creation
  - key/value pair

Extending the code to be more dynamic/flexible and useful.






.. raw:: html

    <embed>
       <br>
    </embed>










`Moving forward to Lesson 8 <lesson_8.html>`__

`Moving back to Lesson 6 <lesson_6.html>`__