#!/usr/bin/python
# ----------------------------------------------------------
"""Program showing the basic use of dictionaries"""

__author__ = "José Edgardo Morales Barroso"
# ----------------------------------------------------------

print("\n------------- Trying Basic Dictionaries -------------\n")
number_dic_en_sp = {1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5:"cinco"}
fruits_dic_en_sp = {"apple":"manzana", "grape":"uva", "banana":"plátano", "strawberry":"fresa"}

print("How to say 1 in Spanish? ", number_dic_en_sp[1])
print("How to say strawberry in Spanish? ", fruits_dic_en_sp["strawberry"])
print("All the fruits in English: ", fruits_dic_en_sp.keys())
print("All the fruits in Spanish: ", fruits_dic_en_sp.values())
print("\n------------- --------------------------- -----------\n")