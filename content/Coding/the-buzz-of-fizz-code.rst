The Buzz of Fizz code
#####################
:date: 2012-12-19 03:30
:author: Ed Rantanen
:category: coding
:slug: the-buzz-of-fizz-code
:status: published

| Update on this:
|  Added tcl and c# to the group!
| Enjoy

A friend was joking with me today about a simple test The BuzzFizz test,
hmm?

It is a simple test to find in 100 iterations the multipliers of 3 & 5
and the combinations of the two.

I wrote up two quick takes on it with a while instead of a for loop.

I ran both of these on -  3.2.0-34-generic-pae #53-Ubuntu

| In C:
| #include <stdio.h>

int main() {

|   int i = 100;
|   int f3,f5;
|   char \*flag;

|   while(i != 0) {
|     f3 =i%3;
|     f5 =i%5;

|     if(f3 == 0 && f5 == 0) {
|        flag = "combo";
|     }else if(f3 == 0) {
|        flag = "fuzz";
|     }else if(f5 == 0){
|        flag = "buzz";
|     }else{
|       flag = "nothing";
|     }

|   printf("%d  %sn",i, flag);
|   --i;
| }

In Perl:

#! /usr/bin/perl -w

  $i = 100;

|   while($i != 0) {
|     $f3 =$i%3;
|     $f5 =$i%5;

|     if($f3 == 0 && $f5 == 0) {
|        $flag = "combo";
|     }elsif($f3 == 0) {
|        $flag = "fuzz";
|     }elsif($f5 == 0){
|        $flag = "buzz";
|     }else{
|       $flag = "nothing";
|     }

|   print("$i t$flagn");
|   --$i;
| }

 In TCL:

 #! /usr/bin/tclsh

| # a simple  tcl version of fizzbuzz
| # prints out
| #      on multiples of 3 prints fizz
| #      on mulitples of 5 prints buzz
| #      on combined multiples of 3&5 fizzbuzz

| set i 100
| set flag " "

|  while {$i != 0} {
|   
|       set f3  [expr { $i % 3}]
|       set f5  [expr { $i % 5}]

|   if {$f3 == 0 && $f5 == 0} {
|           set  flag  "fizzbuzz"
|    } elseif {$f3 == 0} {
|           set flag "fizz"
|    } elseif {$f5 == 0} {
|           set flag "buzz"
|    } else {
|           set flag "  "
|    }
|        

  puts "$i t$f3 t$flag"

|   incr i -1
|  }

|  In C#:
| using System;

| namespace fizzbuzz
| {
|     class MainClass
|     {
|         public static void Main (string[] args)
|         {
|            
|             int i = 100;
|             int f3, f5;
|             string flag;
|            
|             while(--i != 0 ) {
|            
|                 f3 = i % 3;
|                 f5 = i % 5;
|                
|             if(f3 == 0 && f5 == 0) {
|                     flag = "fizzbuzz";
|             }else if(f3 == 0) {
|                     flag = "fizz";
|             }else if(f5 == 0) {
|                     flag = "buzz";
|             }  else {
|                     flag = null;
|             }
|         if(flag != null){
|                Console.WriteLine (" {0}" +"t" +"{1}", i, flag);
|                 }
|                 //--i;
|             }
|         }
|     }
| }
