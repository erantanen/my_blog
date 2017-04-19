#! /usr/bin/env python


# from https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Boolean_Expressions

a = 6
b = 7
c = 42

print(1, a == 6)
print(2, a == 7)
print(3, a == 6 and b == 7)
print(4, a == 7 and b == 7)
print(5, not a == 7 and b == 7)
print(6, a == 7 or b == 7)
print(7, a == 7 or b == 6)
print(8, (not a == 7 and b == 6))

print(9, not a == 7 or not b == 6)
