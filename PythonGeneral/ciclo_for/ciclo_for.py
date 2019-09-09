#!/usr/bin/python
#------------------------------------------------------
"""Program which show the us of for loop"""

__author__ = "José Edgardo Morales Barroso"
__email__ ="joseedgardomb@gmail.com"
#------------------------------------------------------
print("\n----------------- Trying while loop ----------------\n")
try:
    number = int(input("What multiplication table do you want? "))
except ValueError:
    print("Must be an Integer Number")
else:
    for i in range(1,10+1):
        print("{} x {} \t= {}".format(number, i, number * i))
    else:
        print("\nBye for now!\n")

print("\n----------------- ----------------- ----------------\n")