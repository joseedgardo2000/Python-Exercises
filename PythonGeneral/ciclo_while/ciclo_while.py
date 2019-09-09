#!/usr/bin/python

#---------------------------------------------------
"""Program which shows how to use while loop"""

__author__="José Edgardo Morales Barroso"
#---------------------------------------------------

print("\n----------------- Trying while loop ----------------\n")
message = input("Write a message to the humanity: ")
try:
    ntimes = int(input("How many times do you want to repeat it? "))
except ValueError:
    ntimes = 0
else:
    count = 1
    print("\n Sending Message to Humanity....\n")
    while count <= ntimes:
        print("{}: Your message to the humanity is: '{}'".format(count,message))
        count+=1
    else:
        print("\nNothing more to say\n Bye for now!!")

print("\n----------------- ----------------------------------\n")