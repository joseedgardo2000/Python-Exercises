#!/usr/bin/python

# ----------------------------------------------------
"""Program which shows the use of conditionals"""

__author__ = "José Edgardo Morales Barroso"
__email__ = "joseedgardomb@gmail.com"
# ----------------------------------------------------

print("\n----------------- Trying Conditional if ----------------\n")

value = input("Introduce a value: ")

if value.isnumeric():
    print("The value '{}' is a number".format(value))
    fvalue= float(value)
    if fvalue < 25:
        print("The value '{:.2f}' is smaller than 25".format(fvalue))
    elif 25 <= fvalue <= 100:
        print("The value {} is between 25 and 100".format(fvalue))
    else:
        print("The value {} is bigger than 100".format(fvalue))    
else:
    print("The value '{}' is NOT a number".format(value))

print("\n----------------- --------------------- ----------------\n")
