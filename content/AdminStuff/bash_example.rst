bash example
############
:date: 2017-08-7 23:31
:author: Ed Rantanen
:category: AdminStuff
:slug: 1_example
:status: published


.. raw:: html

    <embed>
       <br>
    </embed>



In trouble shooting I need a quick way to visualize some data so wrote a couple of quick and dirty bash scripts.
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