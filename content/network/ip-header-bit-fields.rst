IP Header: Bit fields.
######################
:date: 2014-03-07 18:37
:author: Ed Rantanen
:category: network
:slug: ip-header-bit-fields
:status: published

This is an on going project with sniffing protocols.

Working my way through the IP header I started wonder why many of the
structs have ihl before the version when in the rfc 791 it shows the
version before ihl.  This is the original struct I was playing with also
I noticed that the ihl has a bit field of 5, which did not make sense
since the word length is 8 bits long.

| struct ipheader {
|     unsigned char      iph\_ihl:5, iph\_ver:4;
|     unsigned char      iph\_tos;
|     unsigned short int iph\_len;
|     unsigned short int iph\_ident;
|     unsigned char      iph\_flag;
|     unsigned short int iph\_offset;
|     unsigned char      iph\_ttl;
|     unsigned char      iph\_protocol;
|     unsigned short int iph\_chksum;
|     unsigned int       iph\_sourceip;
|     unsigned int       iph\_destip;
| };

| So I started to play with making some modifcations to a struct, with
  bit fields.
| Used  \ `Low Level Operators and Bit
  Fields <http://www.cs.cf.ac.uk/Dave/C/node13.html>`__   as beginning
  guide.

|  struct ipheader {  
|    unsigned int       iph\_t1:1;
|    unsigned int       iph\_t2:1;
|    unsigned int       iph\_t3:1;
|    unsigned int       iph\_t4:1;
|    unsigned int       iph\_t5:1;
|    unsigned int       iph\_t6:1;
|    unsigned int       iph\_t7:1;
|    unsigned int       iph\_t8:1;

I created a simple printf statement to seen what it all looked like, and
the results at first were a bit confusing. Yes the print statement looks
messy but it works.

| printf("%x%x%x%x%x%x%x%xn", iph->iph\_t1,
|                                                             
  iph->iph\_t2,
|                                                             
  iph->iph\_t3,
|                                                             
  iph->iph\_t4,
|                                                             
  iph->iph\_t5,
|                                                             
  iph->iph\_t6,
|                                                             
  iph->iph\_t7,
|                                                             
  iph->iph\_t8);

result was -> 10100010

| So on the whiteboard broke the result into 4 byte pieces, starting
  from the left.
| 1:2:4:8 \|  1:2:4:8  
| 1:0:1:0 \|  0:0:1:0
|    5              4

The word boundary gets filled from the right moves to the left, this
understand can be used with the rest of the header that has partial word
boundaries such as ecn and flags.
