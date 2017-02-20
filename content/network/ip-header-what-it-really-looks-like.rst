IP Header, what it really looks like.
#####################################
:date: 2012-10-04 15:57
:author: Ed Rantanen
:category: network
:slug: ip-header-what-it-really-looks-like
:status: published

| Started the great experiment on promiscuous mode programing in "c".
| (bit fragmented in thought)

I wasn't sure how working on a Mac inside a VirtualBox vm  running
Ubuntu might work out, but so far things have been rolling along. As
this is giving me a better understanding of how the IP header fits
together as a structure. This is amazing since it is a  structure from
the early 80's and still widely used across the network.

The first thing,

  Build the socket.

::

     sock_raw = socket(AF_INET , SOCK_RAW, IPPROTO_TCP);

  Read from socket.

::

     data_size = recvfrom(sock_raw , buffer , 65536 , 0 , &saddr , &saddr_size);

  I did a simple print to see some results.

|  void Print\_Info(unsigned char\* data , int d\_length)
| {
|      int incr;
|      //data is the buffer from recvfrom
|       for(incr = 0; incr < d\_length ; incr+=2){
|          printf(" %02X%02X ", data[incr], data[incr+1]);
|        }

|      printf("  n");
| }

| Results
| 4500 002C 0C9B 0000 4006 E39C CC5D B228 0A00 020F
  4500 002C 0C9E 0000 4006 EA96 4272 3517 0A00 020F
  4500 002C 0C9F 0000 4006 F659 ADDF BDE5 0A00 020F

And doing this I can see a repition of data, so this made me go and
acutully lookup the RFC for IP. The first one to look at is RFC 791 and
here we can begin to understand the break down of the header. Now the
hard part is to start breaking down the groupings.

4=Ver, 5=IHL, 00=ToS, 002C=TL, 0C9B=ID,  0=Flags, 000=Frag Off,  40=TTL,
06=Prot, EA96=Hdr C\_Sum,  42723517 = Source Address,  0A00 020f =
Destination Address 

::

        0                   1                   2                   3   
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |Version|  IHL  |Type of Service|          Total Length         |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |         Identification        |Flags|      Fragment Offset    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |  Time to Live |    Protocol   |         Header Checksum       |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                       Source Address                          |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Destination Address                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Options                    |    Padding    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| -------------------------------------------------------------------------------------------------------------------------
| This is very short but this is also a continuing experiment, as such
  next step is to breakdown the address into a usable format.
