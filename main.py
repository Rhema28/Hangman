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

# Wrong Guess Counter
wrong_guesses = 0

# Used Letters Tracker
used_letters = []

# Main Loop
print("Welcome to Hangman")
print("Try to Guess the Word")



