# Hangman Game
# Computer picks a word from a list
# Player makes a guess of one letter
# at a time


# imports
import random

# Constants
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

while wrong_guesses < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guesses])
    print("You have used the following letters: ", used_letters)
    print("So far, the word is: ", current_guess)

    guess = input("Enter your letter guess:")
    guess = guess.upper()

    # Check if letter was already used

    while guess in used_letters:
        print("You have already guessed that letter", guess)
        guess = input("Enter your letter guess:")
        guess = guess.upper()
    
    # Add new guessed letter to list of guessed letters
    used_letters.append(guess)

    # Check guess
    if guess in word:
        print("You have guessed correctly!")

    # Give a new version of the word with mixed letters and dashes
    
    new_current_guess = ""
    for letter in word:
        if guess == word[letter]:
            new_current_guess += guess
        else:
            new_current_guess += current_guess[letter]
            print("Sorry that was incorrect")
            # Increase the number of incorrect by 1
            wrong_guesses += 1
        current_guess = new_current_guess

# End the Game
    if wrong_guesses == MAX_WRONG:
        print(HANGMAN[wrong_guesses])
        print("You have been hanged!")
        print("The correct word is", word)
    else:
        print("You have won!")

print(new_current_guess)