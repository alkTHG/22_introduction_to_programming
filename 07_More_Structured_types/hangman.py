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
    print('Welcome to the game Hangman!')
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
    print(f"\nI am thinking of a word that is {len(word)} letters long...")
    return word

# end of helper code
# -----------------------------------

# GLOBAL VARIABLES
secret_word = get_word()
letters_guessed = []
max_guesses = 6
guess = ''
warnings = 3
current_guess = ''

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
        congrats()


def congrats():
    print(f"\nThe word is '{secret_word}'")
    print("Congratulations, you won!")
    print(f"Your total score for this game is: {max_guesses * len(set(secret_word))}")
    another_game()


def another_game():
    global secret_word
    another = input("\nWould you like another game? (y/n)")
    if another not in ['y', 'n']:
        another_game()
    elif another == 'y':
        secret_word = get_word()
        play_hangman()
    elif another == 'n':
        exit(0)


def print_guessed():
    global current_guess
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
    current_guess = to_print
    return to_print


def check_error():
    global max_guesses
    if guess == '*':
        max_guesses -= 1
        print("Possible word matches are:", show_possible_matches(''.join(print_guessed())))
        play_hangman()
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
        print("You have no warnings left so you loose one guess.")
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
    print(f"Good guess: {''.join(print_guessed())}")
    play_hangman()


def not_in_word():
    global max_guesses
    if guess in ['a', 'e', 'i', 'o', 'u']:
        max_guesses -= 2
        print("Oops! That vowel is not in my word. You loose two guesses")
    else:
        max_guesses -= 1
        print("Oops! That letter is not in my word. You loose a guess")
    play_hangman()


def match_the_gap(my_word, other_word):
    my_word = my_word.strip()
    other_word = other_word.strip()
    if len(my_word) != len(other_word):
        return False
    for i, letter in enumerate(my_word):
        if my_word[i] == '-' or my_word[i] == other_word[i]:
            continue
        elif my_word[i] != '-' and my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    matching_words = []
    for word in words_dict:
        if match_the_gap(my_word, word):
            matching_words.append(word)
    return matching_words


def play_hangman():
    global secret_word
    global letters_guessed
    global guess
    print(secret_word)
    word_guessed()
    too_many_turns()
    print(f"\nYou have {max_guesses} guesses left")
    print("Available Letters:", ''.join(set(ascii_lowercase).difference(letters_guessed)))
    print("Hangman Word:", ''.join(print_guessed()))
    guess = input('Guess a letter champ:')
    check_error()
    check_guess()


play_hangman()