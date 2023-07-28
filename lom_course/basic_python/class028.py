
name = input("What's your name: " ).title()
years_old = input('How old you are: ')
years_old = int(years_old)
if name and years_old:
    print(f'Your name is {name}')
    print(f'Your name inverted {name[::-1]}')
    if ' ' in name:
        print('There are spaces in your name')
    else:
        print('There are no spaces in your name')
    print(f'There are {len(name)} characters in your name')
    print(f'The first character of your name is {name[0]}')
    print(f'The last character of your name is {name[-1]}')
else:
    print('Sorry you left requirements empty')