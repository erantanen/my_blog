Radix and Patricia Trie
#######################
:date: 2013-02-28 01:17
:author: Ed Rantanen
:category: coding
:slug: radix
:status: published

 

I am trying to get some thoughts in-line to start working on a Radix
Tree with binary numbers, so the first step was to create a simple
decimal to binary trial.  I am still playing with the approach. The next
step is to take the binary conversion and push it into its own module to
begin a mass conversion. Once we have a mass of binary numbers we can
begin to use the bucket for sorting into a Trie.

First one if ran is correct but backwards.

| #include <stdio.h>
| int num = 137;
| main() {
| int rem, count = 0, increment;
| int binNum[20];

printf(" origanl number %d n", num);

| while(num > 0){
| rem = num % 2;
| binNum[count] = rem;
| printf(" %d : ", count);
| printf(" %d : ", rem);

| num = num/2;
| printf("%dn", num);
| count++;
| }
| }

| And the second one has the numbers in the correct order.
| #include <stdio.h>

int num = 137;

main() {

| int rem, count = 0, i;
| int binNum[9];

| while(num > 0){
| rem = num % 2;
| binNum[8 - count] = rem;
| printf("%d:%d ", 8-count, rem);

| num = num/2;
| count++;
| }

| printf("nn");
| for(i=0;i<count;i++) {
| printf("%d",binNum[i+1]);

| }
| printf("n%d", count);
| printf("nn");

}
