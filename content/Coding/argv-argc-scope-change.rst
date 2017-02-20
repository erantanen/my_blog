argv & argc Scope Change
########################
:date: 2014-03-06 23:30
:author: Ed Rantanen
:category: coding
:slug: argv-argc-scope-change
:status: published

For a project that I am working on had to come up with a simple way to
move argv/argc into a function for use with geopt in c.

This site has a great breakdown of how to build getopt  `C: getopt
Example <http://linuxprograms.wordpress.com/2012/06/22/c-getopt-example/>`__

 Now I am looking at pushing it into a function to make the code more
modular and below is  a quick prep moving argv and argc outside of main.

#include <stdio.h>

| char \*\*global\_argv;
| int global\_argc;

| int f(){
| printf("%s %d  n", global\_argv[0],global\_argc );
| }

| int main(int argc, char \*argv[]){
|   global\_argv = argv;
|   global\_argc = argc;

| f();
| }
