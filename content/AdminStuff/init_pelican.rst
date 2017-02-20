WordPress to Pelican
####################
:date: 2017-02-05 18:40
:author:  Ed Rantanen
:category: Web Testing
:slug: Pelican
:status: published



Working my way through Pelican installation,  followed several tutorials, some varying success. A learning process but a fun one at that. The pelicanconf.py and Makefile are very expandable one of the mods I did in the Makefile.

.. code-block:: c 

     build:
       $(MAKE) clean
       $(MAKE) html
       -cp -R code_snips output/code_snips/


A mini-build got tired of doing make clean then make html along with moving a snips file into output. This is quick dirty and works!

Will begin to clean up the rest of the site in the next couple of weeks, work in progress. 



