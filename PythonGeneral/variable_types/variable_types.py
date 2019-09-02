#!/usr/bin/python

# ----------------------------------------------------------
"""Program which show the simple use of some variables"""

__author__ = "José Edgardo Morales Barroso"
# ----------------------------------------------------------

print("------------Integer------------\n")
a = 100
b = 300
c = a + b
print("a + b = ", c, "\n")

print("---------------Float-----------\n")
d = c / 1000
print("c / 1000 = ", d, "\n")

print("---------------String----------\n")
print("This is a String: ", "\"String is Cadena in Spanish\"", "\n")

print("--------------- Multiple Assignment ----------\n")
aa, bb, cc, dd, ee = "The cat have", 30, "toys and", .5, "cookies"
print("[aa, bb, cc, dd, ee = \"The cat have\", 30, \"toys and\", .5, \"cookies\"] can be used to print: ")
print("{} {} {} {} {}\n".format(aa,bb,cc,dd,ee)) 

print("------------- Asigna/Desasigna Números--------\n")

print("Asigna num1 = 1000 : ")

num1 = 1000
print("num1 value: ", num1)

try:
    print("Deleting num1: ", num1)
    del num1
    print("num1 deleted value is: ", num1)
except NameError:
    print("Certainly [print(\"num1 deleted value is: \", num1)] failed\n")









