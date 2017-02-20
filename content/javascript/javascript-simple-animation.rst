javascript simple  animation
############################
:date: 2014-05-22 23:24
:author: Ed Rantanen
:category: javascript
:slug: javascript-simple-animation
:status: published

| Okay, everybody loves animation here is a simple ball moving in a
  diagonal pattern across the canvas. Using some simple addition a quick
  mod to x & y co-ordinates can be made.
|
 `circle animation <./code_snips/an_circle_simple.htm>`__


``  dx += 10;   dy += 10;``

| The first silly thing I learned was that the timing is not what makes
  the animation, but the ability to clear the canvas before the next
  draw. We do that with
| ``function clear() {   ctx.clearRect(0, 0, width, height); }``

Slowing the animation down is actually quite easy when adjusting
setInterval right now it is at 20 but if you increase it say by 5 to 25
you will see a significant difference. Now that the myCircle is a
function it can be re-used, the same for clear and init.

| Now lets make it a bit more complicated!
| `2 rectangles  animated <./code_snips/an_rec_simple.htm>`__
  
  
  
| I have created another function for rectangles.
| ``function myRect(x,y,w,h,c){  ctx.fillStyle=c;  ctx.fillRect(x,y,w,h);  ctx.stroke(); }``
| And if you notice the c for input, it is for color.
| var c = "#000080";

  code-block:: python
   function myRect(x,y,w,h,c){  
     ctx.fillStyle=c;
     ctx.fillRect(x,y,w,h);
     ctx.stroke(); }


| And if you notice the c for input, it is for color.
| var c = "#000080";

This is still simple but if you look at the code, now you can begin to
see movement in different directions along with change in color for each
rectangle.

There are some problems with this code, it works but it does not take
canvas size into consideration, also both rectangles are using the same
setInterval. That will be another post.
