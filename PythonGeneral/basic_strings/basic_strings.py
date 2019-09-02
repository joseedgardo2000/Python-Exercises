#!/usr/bin/python
# ----------------------------------------------------------
"""Program showing the basic use of the strings"""

__author__ = "José Edgardo Morales Barroso"
# ----------------------------------------------------------

print("------------- Trying Basic String ------------\n")

sentence = "The cat drinks tequila"

print("sentence: \t[{}]\n".format(sentence))
print("Subject: \t[{}]".format(sentence[:7]))
print("Verb: \t\t[{}]".format(sentence[8:14]))
print("Object: \t[{}]".format(sentence[15:]))
print("Double verb: [{}]\n".format(sentence[8:15]*3))

print("------------- -------------------- -----------\n")