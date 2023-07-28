""" Calculator while loop """


# This is how I made the calculator using the 'map' function...


while True:

    while True:
        try:
            operation = input('Enter your operation: ').split()
            number_1, number_2 = map(float, [operation[0], operation[2]])
            break
        except:
            print('Use numbers, in the format >> [x * x] <<')

    while True:       
        if operation[1] == '+':
            print(number_1 + number_2)
            break
        elif operation[1] == '-':
            print(number_1 - number_2)
            break
        elif operation[1] == '*':
            print(number_1 * number_2)
            break
        elif operation[1] == '/':
            print(number_1 / number_2)
            break
        else:
            print('Unexpected error.')

    exit_program = input('Do you want to exit? [y]es or [n]o: ').lower().startswith('y')

    if exit_program is True:
        break
    

"""
# Teacher's answer

while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter the operator (+-/*): ')
    
    valid_numbers = None
    number_1_float = 0
    number_2_float = 0
    
    
    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None
        
    if valid_numbers is None:
        print('One or both of the numbers entered are invalid.')
        continue
    
    allowed_operators = '+-/*'
    
    if operator not in allowed_operators:
        print('Invalid operator.')
        continue
    
    if len(operator) > 1:
        print('Enter only one operator.')
        continue
    
    print()
    
    if operator == '+':
        print(number_1_float + number_2_float)
    if operator == '-':
        print(number_1_float - number_2_float)
    if operator == '*':
        print(number_1_float * number_2_float)
    if operator == '/':
        print(number_1_float / number_2_float)
        
    exit_program = input('Do you want to exit? [y]es: ').lower().startswith('y')

    if exit_program is True:
        break

"""