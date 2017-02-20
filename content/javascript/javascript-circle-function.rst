javascript circle function
##########################
:date: 2014-05-20 00:48
:author: Ed Rantanen
:category: javascript
:slug: javascript-circle-function
:status: published

After creating a simple circle in the previous post, it is time to make
a function so we can call it again and again and again (rince and repeat) you get the
point. Since this is a circle, I am just worried about x & y co-ordinates on the canvas 
along with a radius.

So the call to the function myCircle is at 100(x) 100(y) with a
radius(50). You can play with the 
`Single Circle <./code_snips/f_circle.htm>`__ , its not very
exciting.

`` var c=document.getElementById("myCanvas"); var ctx=c.getContext("2d");``

.. code-block:: javascript

    function myCircle(x,y,r){
      var start = 0;
      var finish = 2\*Math.PI;
      ctx.beginPath();
      ctx.arc(x,y,r,start, finish);
      ctx.stroke();
     }

 myCircle(100,100,50)


 

Now lets have a bit more fun with this function. We can take myCircle
add some random values to x and y. This random placement can come into play if a random fill, 
maybe showing some random snow fall; with y always decreasing. 

`` var c=document.getElementById("myCanvas"); var ctx=c.getContext("2d");``

.. code-block:: javascript

     function myCircle(x,y,r){
       var start = 0;
       var finish = 2\*Math.PI;
       ctx.beginPath();
       ctx.arc(x,y,r,start, finish);
       ctx.stroke();
     }

     for(var incr=0; incr< 50; incr+=3){
      var rxMov = (Math.random() \* 100)\*2;
      var ryMov = (Math.random() \* 100)\*2;
      myCircle(100+rxMov,100+ryMov,20)
     }

| As you can see we have added Math.random to both the x and y, then
  call the function.
| Try it `Random   Circles <./code_snips/f_circle_random.htm>`__
| Hmm, still pretty blah. We will stop there ... but the next will show?
  random colors? And maybe a better use of the canvas area.
