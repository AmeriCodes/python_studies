"""
Create a game for the user to guess the secret word.
You will provide any secret word and give the user the opportunity to input only one letter.
When the user enters a letter, you will check if the entered letter is in the secret word.
If the entered letter is in the secret word, display the letter.
If the entered letter is not in the secret word, display *.
Keep track of the user's attempts.
"""

import os

secret_wold = 'WOMAN'
guessed_letter = ''
attempts = 0


while True:
    
    letter = input('Type a letter: ').upper()
    attempts += 1
    
    if len(letter) > 1:
        print('Type only one letter.')
        continue
    
    if letter in secret_wold:
        guessed_letter += letter
        
    formatted_work = ''
    for secret_letter in secret_wold:
        if secret_letter in guessed_letter:
            formatted_work += secret_letter
        else:
            formatted_work += '*'
    
    print('Formed word:', formatted_work)
    
    if formatted_work == secret_wold:
        os.system('cls')
        print('YOU WON! CONGRATULATIONS!')
        print('The word was', secret_wold)
        print('Attempts:', attempts)
        guessed_letter = ''
        attempts = 0
        break        

"""
GPT answer:

import random

def guess_word():
    secret_word = "elephant"
    guessed_letters = []
    attempts = 0

    while True:
        print("Guess a letter:")
        letter = input().lower()
        attempts += 1

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(letter)

        if letter in secret_word:
            print("Correct guess!")
        else:
            print("*")

        displayed_word = ""
        for char in secret_word:
            if char in guessed_letters:
                displayed_word += char
            else:
                displayed_word += "*"

        print("Current progress:", displayed_word)

        if displayed_word == secret_word:
            print("Congratulations! You guessed the word.")
            print("Total attempts:", attempts)
            break

guess_word()

"""