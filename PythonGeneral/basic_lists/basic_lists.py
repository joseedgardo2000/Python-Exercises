#!/usr/bin/python
# ----------------------------------------------------------
"""Program showing the basic use of lists"""

__author__ = "José Edgardo Morales Barroso"
# ----------------------------------------------------------

print("------------- Trying Basic Lists -------------\n")

bag_content    = ["egg",  5, "money",  7.5, "bread", 2]
fridge_content = ["milk", 2, "butter", 3  , "apple", 8]

print("The first product in the bag and its quantity: {}".format(bag_content[:2])) 
print("How much money are there? {}".format(bag_content[3]))
print("are there other things? {}".format(bag_content[4:]))
print("The contents of 2 bags: {}".format(bag_content * 2))
print("The things in your bag putting the things from the fridge into: \n\t{}\n".format(bag_content+fridge_content))

print("------------- -------------------- -----------\n")