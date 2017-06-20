Flask: a mini web front end
###########################
:date: 2014-08-05 02:06
:author: Ed Rantanen
:category: web testing
:slug: flask-a-mini-web-front-end
:status: published



.. raw:: html

    <embed>
       <br>
    </embed>


I started to work on a project that needed to offer up a couple of data
structures in a json format in a very simple method. This is part of
mechanism using `vis.js <http://visjs.org/>`__ inside of `trac's
wiki <http://trac.edgewall.org/wiki/TracWiki>`__. With a bit of reading
installing vis.js into trac wasn't to difficult, and it works pretty
good to boot!

| So the next phase is to get `Flask <http://flask.pocoo.org/>`__
  working. First a couple of steps that are pretty straight forward
  depending on your os. I did the initial build in Ubuntu, but have also
  done it in OS X as well.
| If you don't have python get it. Then a quick couple of steps after
  that.


.. code-block:: c

 sudo easy_install pip
 pip install flask
 pip install flask-cors


    | "easy\_install" is part of python's setuptool mechanism.
    | "pip" is a python package manager of sorts.
    | "cors" is for Cross Origin Resource Sharing (more on that later)


 Once these are installed, open up a text editor and type/paste in a
  "hello world"

.. code-block:: c

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()



| Save the file as hello.py and on the command line when you put it
  together you get.

.. code-block:: c

 $ python hello.py
 \* Running on http://127.0.0.1:5000/
 127.0.0.1 - - [04/Aug/2014 21:49:35] "GET / HTTP/1.1" 200 -




Open up a browser enter in either 127.0.0.1:5000 or localhost:5000
 The address:port is default at 5000.

| By changing the code a little bit you can begin to see many
  possibilities.
| ``app.run(port=40000)``


.. code-block:: c

 $ python hello.py
 \* Running on http://127.0.0.1:4000/
 127.0.0.1 - - [04/Aug/2014 21:52:33] "GET / HTTP/1.1" 200 -

So we just changed the port, you can change the default host as well.

Just a quick little intro, have fun and expand on the hello world.
