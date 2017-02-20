javascript  with multiple circles having random colors
######################################################
:date: 2014-05-20 23:34
:author: Ed Rantanen
:category: javascript
:slug: javascript-with-multiple-circle-having-random-colors
:status: published

If you look at the random circles and the random circles with colors, a
bit of refactoring can be seen with regard to the Math.random.
Math.floor was added to round down the decimal to an integer. Also the
sizing has changed, as you run refresh you can see the printed result
for both x and y.

Visually the big thing is the color fill. A random hex number is built
and then applied to the fillStyle before the circle is built, once the
circle is built, it is filled then then stroke is completed.

A note on the number
`16777215 <http://www.smashingmagazine.com/2012/10/04/the-code-side-of-color/>`__
it is a mathematical sum of the 24-bit color scheme.

| `Random
  Colors <./code_snips/f_circle_random_colors.htm>`__
  
.. code-block:: javascript

    function myCircle(x,y,r){  
     var ranColor = '#'+ Math.floor(Math.random() * 16777215).toString(16); 
     var start = 0;  var finish = 2*Math.PI;
       ctx.fillStyle = ranColor;
       ctx.beginPath();
       ctx.arc(x,y,r,start, finish); 
       ctx.fill(); 
       ctx.stroke(); 
     }

