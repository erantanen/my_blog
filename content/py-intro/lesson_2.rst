PY-Into 2
#########
:date: 2017-04-1 22:48
:author: Ed Rantanen
:category: py-intro
:slug: lesson_2
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>



comments
........
| pound sign
| 3 back ticks
| example of comments:
 `example: comments <./code_snips/comment.py>`__


variables
.........

bag_full_of_candy = 5

box = bag_full_of_candy * 5

       | x = 2
       | y = 4


data structures
...............


tuple : position =(x,y)

list  :
       | routes = []
       | routes.append(position)



*Note:* Latitude is "0" at equator, "90" north pole / "-90" at south pole

dictionary :
            | fisheries_area = {}
            | fisheries_area["cod"] = (x,y)


.. raw:: html

    <embed>
       <br>
    </embed>



conditionals
............

Decision making, the "If" statement, it is based on some type of boolean logic or algebra.
What is Boolean algebra?


`Boolean algebra is the branch of algebra in which the values of the variables are the
truth values true and false, usually denoted 1 and 0 respectively.`

from `Boolean algebra wiki <https://en.wikipedia.org/wiki/Boolean_algebra>`__
for `Python specific Boolean <https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Boolean_Expressions>`__

 | Test code of boolean logic `boolean prints <./code_snips/boolean_test.py>`__




As we look at dynamic code, variables are not static so the information we set has to be evaluated.

Such as a number value.

if an incoming argument is 5.

we might have statements looking for something less than 4 but if it is equal do something else.

      | if argument < 4:
      |     print("less than 4")
      | elif argument == 4:
      |     print("equals 4)
      | else:
      |     print("greater than 4")













.. raw:: html

    <embed>
       <br>
    </embed>

`Moving forward to Lesson 3 <lesson_3.html>`__

`Moving back to Lesson 1 <lesson_1.html>`__