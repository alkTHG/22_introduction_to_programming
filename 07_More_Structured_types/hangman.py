# Name:
# MIT Username:
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from collections import Counter

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print( "  ", len(wordlist), "words loaded.")
    print('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word

# end of helper code
# -----------------------------------

# GLOBAL VARIABLES
secret_word = get_word()
letters_guessed = []
max_guesses = 6
guess = ''
warnings = 3

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed
    secret_set = set(secret_word)
    guessed_set = set(letters_guessed)
    if secret_set.issubset(guessed_set):
        print("Congratulations, you won!")
        exit(0)


def print_guessed():
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet.
    '''
    global secret_word
    global letters_guessed
    to_print = []
    for letter in secret_word:
        if letter in letters_guessed:
            to_print.append(letter)
        else:
            to_print.append('-')
    return to_print


def congrats():
    pass


def check_error():
    if guess not in list(ascii_lowercase):
        non_letter()
    elif guess in letters_guessed:
        already_guessed()


def already_guessed():
    global warnings
    print("Oops! You've already guessed that letter. ")
    warnings -= 1
    warning_check()


def non_letter():
    global warnings
    warnings -= 1
    print("Oops! That is not a valid letter. ")
    warning_check()


def warning_check():
    global max_guesses
    global warnings
    if warnings == -1:
        max_guesses -= 1
        warnings = 3
        print(f"You have no warnings left so you loose one guess. You have {max_guesses} guesses left")
    else:
        print(f"You have {warnings} warnings left:")
    play_hangman()


def next_turn():
    play_hangman()


def too_many_turns():
    if max_guesses < 1:
        print(f"Sorry you ran out of guesses. The word was {secret_word}")
        exit(0)


def check_guess():
    global guess
    letters_guessed.append(guess)
    if guess not in secret_word:
        not_in_word()
    play_hangman()


def not_in_word():
    global max_guesses
    max_guesses -= 1
    print("Oops! That letter is not in my word")
    play_hangman()


def play_hangman():
    global secret_word
    global letters_guessed
    global guess
    print(secret_word)
    word_guessed()
    too_many_turns()
    print(f"\nYou have {max_guesses} guesses left")
    print("Available Letters:", set(ascii_lowercase).difference(letters_guessed))
    print("Hangman Word:", print_guessed())
    guess = input('Guess a letter champ:')
    check_error()
    check_guess()



play_hangman()