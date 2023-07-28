Due to my short experience in another course, I avoided uploading very basic information and exercises. Instead, I chose to create a Readme file solely for notes on small tricks and things I didn't know about Python, reserving the .py files exclusively for exercises and projects from the course.

```python
# This is a comentary function

"""This is a DocString """

"""Docstrings are documentation strings in Python, used to describe objects such as functions, classes, or modules. They can be accessed at runtime and provide detailed information about the usage and behavior of the object.

Comments, on the other hand, are snippets of text added to the code to provide explanations or annotations to programmers. They are ignored by the Python interpreter and have no impact on program execution.

In summary, docstrings are for documentation, accessible at runtime, while comments are for clarification purposes and are ignored by the Python interpreter."""
```

The 'print' function displays something on the screen. It can accumulate multiple arguments by separating them with commas. By default, Python will add a space between the arguments, but this can be changed using the 'sep="?"' command, where whatever is placed inside the quotation marks will be used as a separator. The 'end=''' command is used to prevent line breaks.


```python
# \r\n = CRLF
print(52, 40)
print(12, 34, 1011, sep="-", end='##\r\n')
print(56, 78, sep='-', end='\n')
print(52, 44, end='') # Here, since there is nothing between the quotation marks, Python does not break the line and continues with the next command.
print(9, 10, sep= '&&')
```
Python = Programming language
Type of typing = Dynamic / Strong
str -> string -> text
Strings are texts that are enclosed in quotation marks

```python
# Single quotes
print('Mateus Américo')
print(1, 'Mateus "Américo"')

# Doble quotes
print("Mateus \"Américo")
print(1, "Mateus 'Américo'")

# Escape
print("Mateus \"Américo\"")

# r
print(r"Mateus \"Américo\"")
```

```python
# int -> Integer
# The int type represents any positive or negative whole number.
# An unsigned int is considered positive.

print(11) # int
print(-11) # int
print(0) # int

# float -> Floating-point number
# The float type represents any positive or negative number with a decimal point.
# An unsigned float is considered positive.
print(1.1, 10.11) # float

# The type() function shows the type that Python inferred for the value.
print(type('Américo'))
print(type(1))
print(type(-1))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
```


In addition to integers and floats, another commonly used primitive type is the boolean type. The boolean type represents a logical value and can have two possible values: True or False. Booleans are often used in conditional statements and logical operations to control the flow of a program.

```python
print(10 == 10)
print(10 == 11)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))
```

Values such as 0, 0.0, and '' are considered false, and there is also the None type, which is used to represent a non-value.

Short-circuit evaluation using 'or'
```python	
password = input('Password: ') or 'No password entered'
print(password)
```

### Basic string interpolation:

s - string
d and i - integer
f - float
x and X - hexadecimal (0123456789ABCDEF)

```python	
name = 'Américo'
price = 1155.45678
variable = '%s, the price is $%.2f' % (name, price)
print(variable)
print('The hexadecimal of %d is %04X' % (256, 256))
```

### f-strings
```python	
variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}') #padding
print(f'{variable: <10}') #  ''
print(f'{variable: ^10}') #  ''
print(f'{1188.1982374578:h>+10,.1f}') # output>    hh+1,188.2 
print(f'{1188.1982374578:x=+12,.1f}') # output>    +xxxx1,188.2
print(f'The hexadecimal of 1500 is {1500:X}') # output>     The hexadecimal of 1500 is 5DC
```

### Assignment Operators 

Assignment: =
Addition: +=
Subtraction: -=
Multiplication: *=
Division: /=
Floor Division: //=
Modulo: %=
Exponentiation: **=
Bitwise OR: |=
Bitwise AND: &=
Bitwise XOR: ^=
Left Shift: <<=
Right Shift: >>=


### while/else

In Python, using else with while is a specific construct that allows executing a code block when the while condition becomes false. The else clause is executed only if the while loop is completed normally, meaning if the while condition becomes false.

This while-else structure can be useful to perform a specific action after iterating through all the elements of a while loop, without the need for an additional control variable to check if the loop was successfully completed.

```python
""" while/else """
string = 'Any value'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)
    i += 1
else:
    print('No space found in the string.')
print('Outside the while loop.')
```

In this context, else in while serves to execute a specific code block when the while condition is not interrupted by a break statement. In the provided example, the else block is triggered if no space is found in the string during the loop.

If there is a break statement inside the while, the code block under else will not be executed as the execution of the loop was abruptly terminated.

### Doble-precision floating-point format IEEE 754
```python
import decimal

number_1 = decimal.Decimal("0.1")
number_2 = decimal.Decimal("0.7")
number_3 = number_1 + number_2

print(number_3)
print(f'{number_3:.2f}')
print(round(number_3, 3))
```

### Python Interpreter

python mod.py (execute the mod)
python -u (unbuffered)
python -m mod (module as a script)
python -c 'cmd' (command)
python -i mod.py (interactive with mod)


## The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!