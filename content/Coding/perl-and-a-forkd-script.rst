perl and a fork'd script
########################
:date: 2012-01-26 21:14
:author: Ed Rantanen
:category: coding
:slug: perl-forked
:status: published

I had created an expect script the other day that was to gather some
data, the script ran well but at times because of timing issues strange
things seemed to happen with the data. So I broke the script apart and
then built a launcher script in perl. This script launches or spawns
individual expect scripts that are gathering data. 

The ability to fork in perl and launch a secondary script is quite
useful.

 #! /usr/bin/env perl

|  @ip\_list = qw(10.0.0.1 10.0.0.2 10.0.0.3);
|  
|   foreach $ip (@ip\_list) {
|        my $pid = fork();
|       if ($pid) {
|      # parent
|        push(@childs, $pid);
|       } elsif ($pid == 0) {
|         # child
|         # a command to that is launch into its own shell
|         exec "./ssl\_vpn\_fetch.tcl $ip $passwd $user";      
|         sleep 5;
|         exit(0);
|     } else {
|       die "couldn.t fork: $!n";
|     }
|   }

|     foreach (@childs) {
|     waitpid($\_, 0);
|     }
