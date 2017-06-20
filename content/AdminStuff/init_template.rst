A template for an init script
#############################
:date: 2017-06-01
:author:  Ed Rantanen
:category: AdminStuff
:slug: init_script
:status: published

.. raw:: html

    <embed>
       <br>
    </embed>





jenkins
.......


Started working on an init.d script to launch a Jenkins slave.jar today.
Its interesting as the command line for firing it off is a bit crazy.

A simple example of the console `slave.jar <https://wiki.jenkins-ci.org/display/JENKINS/Launching+slave.jar+from+from+console>`_

The init script is written in bash to simplify compatibility in doing that we now have some limitations but having fun with it.

.. code-block:: c

     full_command="${LOCAL_JAVA_PATH} -jar \
                ${AGENT_EXECUTION_DIR}/$JENKINS_AGENT_BIN_NAME -jnlpUrl \
                ${JENKINS_MASTER_COMPUTER}/${AGENT_NAME}/slave-agent.jnlp \
                -jnlpCredentials $JENKINS_TOKEN"



.. raw:: html

    <embed>
       <br>
    </embed>






There is a config file associated with "full_command" makes life a bit easier in setting up.

   | ". /app/jenkinsAgent/admin/agent.cfg"


The full script is here `init_template <./code_snips/init_template>`__





.. code-block:: c

    function GRAB_PID()
    {
      local  PID=`ps -ef | grep 'java -jar.*slave.jar\|[j]ava -jar slave.jar' |\
                  grep -v grep | \
                  awk '{print $2}'`
      echo    "$PID"
    }


Created a simple function for PID, have an "or" in the grep and do a quick awk for the print.
To call the function a "$(function name)" is used.

.. code-block:: c

     echo $(GRAB_PID)