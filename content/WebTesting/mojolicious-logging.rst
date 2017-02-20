Mojolicious Logging
###################
:date: 2014-10-14 02:08
:author: Ed Rantanen
:category: web testing
:slug: mojolicious-logging
:status: published

| After playing around with Mojo::Log for a few days I came across this
  great plugin
  `AccessLog <http://search.cpan.org/~graf/Mojolicious-Plugin-AccessLog-0.001/lib/Mojolicious/Plugin/AccessLog.pm>`__.
  Something simple like changing the log name or its location is a bit
  painful in the vanilla Mojo::Log. The format is easy to adjust, if
  using morbo you can make adjustments on the fly and quickly see what
  the results are.
| If no format line is added then output will be:
| ``127.0.0.1 - - [13/Oct/2014:20:28:56 -0400] "GET / HTTP/1.1" 200 137 127.0.0.1 - - [13/Oct/2014:20:28:57 -0400] "GET / HTTP/1.1" 200 137``

| If a format line is added with something simple as this " [%a] - %b"
  output will be\ `` [127.0.0.1] - 137  [127.0.0.1] - 137``
| The link has large list to pick from for the format, have fun.

| Here is are two Mojolicious::Lite examples.
| The first one has the plugin outside of the route.
| ``#!/usr/bin/env perl use Mojolicious::Lite; use warnings;``

| plugin AccessLog => {log => 'log/access.log',
| format=> " %a - %b"
| };

| get '/' => sub {
| my $c = shift;
| $c->render('index');
| };

| app->start;
| \_\_DATA\_\_

| @@ index.html.ep
| % layout 'default';
| % title 'Welcome';
| Welcome to the Mojolicious real-time web framework!

.. raw:: html

   <p>

| @@ layouts/default.html.ep

| 

| 

| 

<%= content %>

| 

.. raw:: html

   </p>

| and the second one has the plugin in side of the route.
| ``#!/usr/bin/env perl use Mojolicious::Lite; use warnings;``

| get '/' => sub {
| my $c = shift;
| $c->render('index');

| plugin AccessLog => {log => 'log/access.log',
| format=> " %a - %b"
| };
| };

| app->start;
| \_\_DATA\_\_

| @@ index.html.ep
| % layout 'default';
| % title 'Welcome';
| Welcome to the Mojolicious real-time web framework!

.. raw:: html

   <p>

| @@ layouts/default.html.ep

| 

| 

| 

<%= content %>

| 

.. raw:: html

   </p>

So now we might think why have it inside of the route? Well depending on
what is getting logged, you might have some special needs that would
require more data gathered for your log? This way you can not only build
a format but then label each route and its log. At the same time an
overall dev/production log can still be built and utilized and/or
archived for parsing at a later date.
