bash scripts  updated
#####################
:date: 2018-12-2 23:31
:author: Ed Rantanen
:category: AdminStuff
:slug: 1_example
:status: published


.. raw:: html

    <embed>
       <br>
    </embed>


`example: bash scriptlets in one file  <./code_snips/bash.htm>`__

The above examples can be put into a file with a copy/paste (one to a file)
    * Name the file something(?)
    * Do a chmod +x on file
    * If you have your own little bin dir put in there (helps if you set-up a path for this)
    * Test it out!


In troubleshooting I needed a quick way to visualize some data scraping, so wrote a couple of quick and dirty bash scripts.
Going to add more as time goes on, will be a mini-repo along with an explain how/what is going on with each script.

The first one will grab a directory to read, and then out-puts size k/m/g/t along with complete path.


.. code-block:: c

    echo "enter directory, press Enter"
    read dir
    array=($(ls  "$dir"))
    echo -e "-----------------------\n"

    for elm in "${array[@]}";
      do
        cat_elm=$(echo ${dir}/${elm})
        if [ -d "${cat_elm}" ]
        then
          output= eval du -sh ${cat_elm}
          echo -n "$output"|tr '\n' ' '
         fi
       done




And example of the output on a mac.

.. code-block:: c

    trident-2:~ edrantanen$ ./bash_test.sh
    enter directory, press Enter
    /usr/local
    -----------------------

    140K	/usr/local/bin
     67M	/usr/local/git
    692K	/usr/local/share








The second script uses locate (making sure that updatedb has been done) along with ls -lh for an output. I used this
recently to look for all the nohup.out files on a system, found more than had first realized existed.


.. code-block:: c

    echo "enter word to find, press Enter"
    read word
    array=($(locate  "$word"))
    echo -e "-----------------------\n"

    for elm in "${array[@]}";
      do
       output= eval  ls -lh "$elm"
       echo "$output" |tr '\n' ' '
      done