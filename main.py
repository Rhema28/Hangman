# Hangman Game
# Computer picks a word from a list
# Player makes a guess of one letter 
# at a time 


#imports
import random

#Constants
HANGMAN = ['''
    +---+
    |   |
        |
        |
        |
        |
===========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
===========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
===========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========''', '''
 +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========''', '''
 +---+
    |   |
    O   |
   /|\  |
   / \    |
        |
===========''']

WORDS = ["HEART", "LOBSTER", "RABBIT", "MOTHERHOOD", "STAR", "PINEAPPLE"]
 
MAX_WRONG = len(HANGMAN) - 1


# Initialise Variables

# Pick a word
word = random.choice(WORDS)

print(word)

# Dashes for each letter in a word
current_guess = "-" * len(word)

print(word)
print(current_guess)