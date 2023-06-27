

questions = [
    {
        'Question': 'What is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

num_correct = 0
for question in questions:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    choice = input('Choose an option: ')

    correct = False
    choice_int = None
    num_options = len(options)

    if choice.isdigit():
        choice_int = int(choice)

    if choice_int is not None:
        if 0 <= choice_int < num_options:
            if options[choice_int] == question['Answer']:
                correct = True

    print()
    if correct:
        num_correct += 1
        print('Correct! 👍')
    else:
        print('Wrong! ❌')

    print()

print('You got', num_correct, 'out of', len(questions), 'questions correct.')
