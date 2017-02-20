Mojolicious::Lite - a cool framework
####################################
:date: 2014-10-07 00:54
:author: Ed Rantanen
:category: web testing
:slug: mojoliciouslite-a-cool-framework
:status: published

| Looking at another Framework, and have been playing with Mojolicious
  for a couple of weeks now, and having a blast with it. This framework
  using the Perl Language. If using the full blown version verses the
  lite you can work in an MVC structure, the lite can be turned into a
  fully structured MVC/MVVM or what ever quite easily.
| Main site has a quick start that is very good -> `Mojolicious
  Home <http://mojolicio.us/>`__

Once I had the framework up and running I asked a couple of quick
questions, what is the diff from the full to the lite? How to make a few
basic tweeks like logs, what goes into them, how to offer up some
`rrd <http://oss.oetiker.ch/rrdtool/>`__ Data and how to get JavaScript
with JSON functioning. Then at some point get the MVC going as well, the
model/view/control is all separated testing and logging are also
included as well, the lite version is all self contained in one file.

| To build either:
| ``$ mojo generate lite_app myapp.pl $ mojo generate app MyAppcode``

| To launch your app use morbo in-front of "myapp.pl" like this.
| ``$ morbo myapp.pl Server available at http://127.0.0.1:3000.``

| Open a browser type in "http://localhost:3000" and there you go!
| But what if you want to try from a different machine? Then try a
  slight variation like this.
  ``./l_myapp.pl daemon -l http://0.0.0.0:80 Server available at http://0.0.0.0:80``
  When you do this though you will have to be either su or do sudo
  otherwise a socket error will be returned (tried from both Red Hat and
  OSX).

This was very short, but it would be easy to start and include the
kitchen sink with some of the things we could answer, so the next one
will be "logs" and a couple of things that I have found.
