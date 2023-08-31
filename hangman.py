'''
hangman
'''

import random

words = ['red', 'ant', 'notes', 'pens', 'tracing']

chosen_word = random.choice(words)

def board(word):
    spaces = len(word)
    print("_ " * spaces)
    print(f'you have {lives} lives')

def play():
    guess = input('Guess a letter or word: ')
    if len(guess) > 1:
        if guess == chosen_word:
            print(f"You guessed it!\nThe word was '{chosen_word}.'")
        else:
            pass
    else:
        pass

lives = 6
tries = 0
board(chosen_word)
play()