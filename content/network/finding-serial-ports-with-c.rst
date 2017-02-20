Finding Serial Ports with C#
############################
:date: 2013-01-03 17:44
:author: Ed Rantanen
:category:  network
:slug: finding-serial-ports-with-c
:status: published

Before starting another project that utilizes an Arduino and a JY-MCU
Bluetooth module,  a quick little experiment was done with C# on
different platforms.  Also I used MonoDevelop and MS Visual Studio as
the build mechanism (to see if they might make a difference as well). 
The quick experiments showed me a couple of things, what the different
os's are able to show of the serial ports with same code, and what is
being offered in the way of data arrays.  Further investigating, which I
do not show here with the System.IO and SerialPort has many different
layers that in themselves deserve quick short write-ups.

The code is very simple:

| using System;
| using System.IO.Ports;
| using System.Linq;

| namespace serial\_test
| {
|     class MainClass
|     {
|         public static void Main (string[] args)
|         {
|             var port\_list = SerialPort.GetPortNames ();

|             foreach (var port in port\_list) {
|                 Console.WriteLine (port);
|             }

|         }
|     }
| }

When ran with Visual Studio on Windows 7, the output was an empty array
of data,  in another version of code on the Win 7 box I checked for null
at different levels. Each time it came back as 0.

.. raw:: html

   <div style="clear: both; text-align: center;">

.. raw:: html

   </div>

This same code ran on OSX is interesting because of the result showing
the Bluetooth

.. raw:: html

   <div style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

 And a the same code ran in Ubuntu inside of Virtual Box VM on OSX.

.. raw:: html

   <div style="clear: both; text-align: center;">

|image1|

.. raw:: html

   </div>

.. raw:: html

   <div style="clear: both; text-align: center;">

.. raw:: html

   </div>

.. |image0| image:: http://pseudopoint.net/wp/wp-content/uploads/2013/01/serial_result3.png
   :target: http://pseudopoint.net/wp/wp-content/uploads/2013/01/serial_result3.png
.. |image1| image:: http://pseudopoint.net/wp/wp-content/uploads/2013/01/serial_result2.png
   :target: http://pseudopoint.net/wp/wp-content/uploads/2013/01/serial_result2.png
