Tokenize Numbers with javascript 
#################################
:date: 2014-05-17 00:32
:author: Ed Rantanen
:category: javascript
:slug: tokenize-numbers-with-javascript
:status: published

| I have been working through some problems at `Project
  Euler <https://projecteuler.net/>`__ mostly in C, but after dorking a
  bit with javascript for another project saw a potential here.
| This Function is very basic, num\_token takes an integer of 121.
| Integer is turned into a string with to "toString".
| String is broken into tokens.

Extra step I have added is to parse the token at position 0 to have an
int again, for later use.

`` function num_token(a){     var incr = 0;     var token = a.toString();     var token_result = token.split("");     var t = parseInt(token_result[incr]);      document.getElementById("output").innerHTML = t + ""; } num_token(121);``

| And why is 121 interesting?
| It is a `Palindromic
  Number <http://en.wikipedia.org/wiki/Palindromic_number>`__

Next step is to add a loop, and see how many Palindromic Numbers you can
find under 1000.
