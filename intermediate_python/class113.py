"""
Create a function that multiplies all the unnamed arguments received, returns the total to a variable, and displays the value of the variable.
"""
def multiply_arg(*args):
    total = True
    for numbers in args:
        total *= numbers
    return total

result = multiply_arg(2,4,5,7,8)
print(result)



"""
Create a function that checks whether a number is even or odd.
Return whether the number is even or odd.
"""

def check_even_odd(number):
    even = number % 2 == 0
    
    if even:
        return f'{number} é Par'
    return f'{number} é Ímpar'


print(check_even_odd(2))
print(check_even_odd(12))
print(check_even_odd(1887))
print(check_even_odd(77998))
