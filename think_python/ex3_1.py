"""
Python provides a built-in function called *len* that length of a string,
so the value os len('allen') is 5.
Write a function named right_justify that takes a sting
named s as parameter and prints the string with
enough leading spaces so that the last letter of
the string is in column 70 of the display.
"""


def right_justify(s):
    print(" " * (70 - len(s)) + s)


right_justify("américo")
