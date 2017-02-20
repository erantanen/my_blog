javascript circle
#################
:date: 2014-05-17 13:10
:author:  Ed Rantanen
:category: greek
:slug: javascript-circle
:status: published

I have been reading through a couple of books by, `Sir Thomas L.
Heath <http://en.wikipedia.org/wiki/T._L._Heath>`__ on Greek
Mathematics. And had an idea that it might be fun to see if I could get
some working geometric shapes going to represent several of the
theorems.

One theorem of interest is by
`Thales <http://en.wikipedia.org/wiki/Thales%27_theorem>`__ an inscribed
right angle inside of a circle.

So how do we make a circle in javascript?

| This is a very basic script(no functions), we build a container which
  is our canvas then point that to an id on the page.
| I have broken out the x&y coordinates and a radius so we can use them
  in calculations at a later date. If we wanted a simple arc, then we
  can adjust the start and finish of the path.

.. code-block:: javascript

     <p> <canvas id="myCanvas"
      width="300"
      height="300"
      solid #d3d3d3;">
      Your browser does not support the canvas tag.
      </canvas></p>

      var c=document.getElementById("myCanvas");
      var ctx=c.getContext("2d");
      ctx.beginPath();
      //circle
      var x = 100;
      var y = 100;
      var r = 50;
      var start = 0;
      var finish = 2\*Math.PI;
      ctx.arc(x,y,r,start, finish);
      ctx.stroke();



To keep this post small and to the point I am not going to add anything
else, but the next phase will be to bisect the circle. This will be a
horizontal line, and using the x&y with the radius can you see how this
might be done?


