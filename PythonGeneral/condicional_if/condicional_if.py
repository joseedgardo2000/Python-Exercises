#!/usr/bin/python

# ----------------------------------------------------
"""Program which shows the use of conditionals"""

__author__ = "José Edgardo Morales Barroso"
# ----------------------------------------------------

print("\n----------------- Trying Conditional if ----------------\n")

value = input("Introduce a value: ")

if value.isnumeric():
    print("The value '{}' is a number".format(value))
else:
    print("The value '{}' is NOT a number".format(value))

print("\n----------------- --------------------- ----------------\n")
