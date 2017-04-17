#! /usr/bin/env python


"""
example showing how to open a file and what to do with non strings


"""




with open("blah.txt", "w") as FH:
    FH.write("Space… the final frontier.")

    for elm in range(10):
        #elm has been cast to a string
        FH.write(str(elm) + "\n")
