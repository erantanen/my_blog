Deploy Pelican with Jenkins
###########################
:date: 2018-03-21 18:40
:author:  Ed Rantanen
:category: AdminStuff
:slug: Pelican
:status: published

Jenkins install
###############

Using Jenkins at work I realized as the light bulb finally went click it should be used to do a make with Pelican
and then a content deploy.

That being said, the first step was to get Jenkins working.

I started looking at several sites that talked about Mac/OS X, and went back to a site I had previously used for work.
There are a few obvious things you will not do, such as yum install java, but this should give a general idea of setup.

`Jenkins Install <https://www.edureka.co/blog/install-jenkins/>`_

There were a few issues, called clean-up (residue) before everything was running.
1. I tried the OSX Jenkins install from the Jenkins website (did not work)
2. When pulling the Tomcat for OSX I did not make sure I had Ver 9.x
        jenkins.war is over 50m and will not work on Ver 7/8
3. Permissions, after pulling/pushing files about OSX had to go back to do chown on several things
4. Java version, made the mistake of upgrading Java to 10 stay with 8
        ls /Library/Java/JavaVirtualMachines/


Gitolite Install
################


brew  install git-core +universal
Create user to host repos ie git?
Within above directory ~/ do mkdir bin
    This preps for the step "Run gitolite/install -ln"
If there is no .profile in the new user's account create one and add.
        export PATH=~/bin:$PATH


http://gitolite.com/gitolite/install/index.html

From the admin account you created, which is separate from the hosting account run:

   git clone git@host:gitolite-admin



Moving an existing repo
#######################

These directions worked to a "T"
http://pressreset.net/2011/10/moving-existing-local-git-repository-into-a-fresh-gitolite-setup/


Git -> Two Remote Heads
#######################

https://gist.github.com/rvl/c3f156e117e22a25f242

Learning, Learning it is better to use the git commands than being inside of the config file.


Single git push
$ more config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
[branch "master"]
[remote "origin"]
        url = git@192.168.254.27:my_blog.git
        fetch = +refs/heads/*:refs/remotes/origin/*

Dual git push
$ git remote show origin
* remote origin
  Fetch URL: git@192.168.254.27:my_blog.git
  Push  URL: https://github.com/erantanen/my_blog.git
  Push  URL: git@192.168.254.27:my_blog.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local ref configured for 'git push':
    master pushes to master (fast-forwardable)
