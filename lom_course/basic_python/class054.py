"""
Write a program that asks the user to enter an integer number and inform whether the number is even or odd. If the user does not enter an integer number, inform that it is not an integer.
"""
number = input('Enter an integer number: ')

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f'{number} is an even number.')
    else:
        print(f'{number} is an odd number.')
else:
    print(f'{number} is not an integer.')
"""
Write a program that asks the user for the hour and, based on the given time, displays the appropriate greeting. Example: Good morning for 0-11, Good afternoon for 12-17, and Good evening for 18-23.
"""
entry = input('Enter the hour: ')

try:
    hour = int(entry)
    
    if hour >= 0 and hour <= 11:
        print('Good morning!')
    elif hour >= 12 and hour <= 17:
        print('Good afternoon!')
    elif hour >= 18 and hour <= 23:
        print('Good evening!')
    else:
        print("I don't know this time!")
except:
    print('Please enter only integer numbers.')

"""
Write a program that asks for the user's first name. If the name has 4 letters or less, write "Your name is short"; if it has between 5 and 6 letters, write "Your name is normal"; if it has more than 6 letters, write "Your name is very long". 
"""
name = input('Enter your first name: ')
name_length = len(name)

if name_length > 1:
    if name_length < 5:
        print('Your name is short.')
    elif name_length < 7:
        print('Your name is normal.')
    else:
        print('Your name is long.')
else:
    print('Enter more letters.')
