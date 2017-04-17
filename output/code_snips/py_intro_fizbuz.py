""" 

initial example of for loop and mod

"""

for a in range(0, 100):
    str_a = str(a)
    mod_a = str(a % 2)
    print(str_a + " : " + mod_a)

################
# if statements
################

bag_full_of_candy = 5
contents = bag_full_of_candy

if contents is None:
    print("I am hungry")
elif contents == 5:
    print("yummy time!")
elif contents < 5:
    print("not enough to share")
else:
    print("next time")
