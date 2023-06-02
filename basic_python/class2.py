"""
The 'print' function displays something on the screen. It can accumulate multiple arguments by separating them with commas. By default, Python will add a space between the arguments, but this can be changed using the 'sep="?"' command, where whatever is placed inside the quotation marks will be used as a separator. The 'end=''' command is used to prevent line breaks.
"""

# \r\n = CRLF
print(52, 40)
print(12, 34, 1011, sep="-", end='##\r\n')
print(56, 78, sep='-', end='\n')
print(52, 44, end='') # Here, since there is nothing between the quotation marks, Python does not break the line and continues with the next command.
print(9, 10, sep= '&&')