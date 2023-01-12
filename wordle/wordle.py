"""A command line wordle game where the user gets to specify the length of the word. """

import random
from colorama import Fore, Style
from utility import (get_word_length, get_users_hint_preference,
get_guess, get_words_of_specified_length, get_dictionary)

# TODO: Adjust the function find_word so that it takes into account how many times a letter
# appears in a word. For example, if the correct word is sleek, and you guess skews, the
# first s will be green while the second s will be grey,
# indicating that there is only one s in the word.



# NOTE: I read that it's bad form to use global variables because it makes your code
# harder to read and it gets messy quicker. In this program, I think it's fine since
# there are only five globals and their function is fairly self evident.

# Sets to contain green, yellow, and eliminated letters.
greens = set()
yellows = set()
eliminated = set()

# This holds letters and positions (zero indexed) in the string format "{letter} {index}"
# for example "h 0" for the word "hello"
greens_and_positions = set()
# This is very similar to the set above, except the position is wrong. So "h 2" for the word "hello"
yellows_and_positions = set()

WORD_LENGTH = get_word_length()
HINT_PREFERENCE = get_users_hint_preference()

def main():

    dictionary = get_dictionary()

    words_of_specified_length = get_words_of_specified_length(dictionary, WORD_LENGTH)

    # Get random word of users specified length
    correct_word = random.choice(words_of_specified_length)

    # Set up the list containing the six guesses that wordle allows.
    guess_size = "_" * WORD_LENGTH
    guesses = [guess_size, guess_size, guess_size, guess_size, guess_size, guess_size]

    # To keep track of how many guesses the user has used
    guess_count = 0

    while True:
        print_six_guesses(guesses, correct_word, WORD_LENGTH)
        print_alphabet()
        # print(find_word(words_of_specified_length))

        if HINT_PREFERENCE:
            if guess_count == 2:
                print_hint(correct_word, WORD_LENGTH)

            # If find_word() returns one word that word must be the correct word,
            # so printing it would give the answer away.
            # So this prints the hint only if find_word() returns more than 1 word.
            if guess_count == 4 and len(find_word(words_of_specified_length)) > 1:
                print(find_word(words_of_specified_length))
                print("Here's some more help, these are all the possible remaining words.")


        guess = get_guess(words_of_specified_length, WORD_LENGTH)

        guesses[guess_count] = guess

        check_green_and_yellow_positions(guess, correct_word)


        guess_count += 1
        if guess == correct_word:
            print_six_guesses(guesses, correct_word, WORD_LENGTH)
            print_alphabet()
            print("RIGHT GUESS! :)")
            break
        if guess_count > 5:
            print_six_guesses(guesses, correct_word, WORD_LENGTH)
            print_alphabet()
            print(f"Out of tries, the word was {correct_word}")
            break

def print_six_guesses(guesses, correct_word, word_length):
    """
    Wordle offers six guesses, where each guess is printed
    consecutively. This function prints the guesses, colour coded.
    """
    # count how many times each letter occurs in the correct word, store data in a dict

    # go through all 6 guesses
    #     go through all the letters of the current guess
    #         if current letter has been used in the guess more times than the letter appears in the correct word
    #             print letter in white
    #         else if current letter is in word and in right spot
    #             print letter in green
    #             add letter to greens
    #         else if current letter is in word but in the wrong spot
    #             print letter in yellow
    #             add letter to yellows
    #         if current letter is not in the word
    #             print letter in white
    #             add letter to eliminated (only if letter is not in the correct word)

    # To count how many times a letter occurs in the correct word.
    letters_count = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
        "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    for letter in correct_word:
        letters_count[letter] += 1

    # This is just so the later function ignores underscores
    letters_count["_"] = word_length


    for i in range(len(guesses)):

        # To store how many times letters occur in the users guess
        guess_letters_count = dict()

        for j in range(word_length):
            # For the sake of simplicity and readability
            current_letter = guesses[i][j]

            # Count the number of times the current letter occurs in the guess
            if current_letter in guess_letters_count:
                guess_letters_count[current_letter] += 1
            else:
                guess_letters_count[current_letter] = 1


            if guess_letters_count[current_letter] > letters_count[current_letter] and current_letter in correct_word:
                print(current_letter, end="")
            elif current_letter == correct_word[j]:
                print(f"{Fore.GREEN}{current_letter}{Style.RESET_ALL}", end="")
                greens.add(current_letter)
            elif current_letter != correct_word[j] and current_letter in correct_word:
                print(f"{Fore.YELLOW}{current_letter}{Style.RESET_ALL}", end="")
                yellows.add(current_letter)
            elif current_letter not in correct_word:
                print(current_letter, end="")
                if current_letter != "_":
                    eliminated.add(current_letter)
        print()

def check_green_and_yellow_positions(guess, correct_word):
    """Checks the guess for yellows and greens, and their positions."""
    for i in range(len(guess)):
        if guess[i] == correct_word[i]:
            greens_and_positions.add(f"{guess[i]} {i}")
        elif guess[i] != correct_word[i] and guess[i] in correct_word:
            yellows.add(guess[i])
            yellows_and_positions.add(f"{guess[i]} {i}")



def print_alphabet():
    """Prints the choices in alphabet the player has."""
    alphabet = ["a", "b", "c", "d", "e", "f", "g",
                "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    # Fore.COLOR sets the text to the chosen color and Style.RESET_ALL resets to the default
    for letter in alphabet:
        if letter in greens:
            print(f"{Fore.GREEN}{letter}{Style.RESET_ALL} ", end="")
        elif letter in yellows:
            print(f"{Fore.YELLOW}{letter}{Style.RESET_ALL} ", end="")
        elif letter in eliminated:
            pass
        else:
            print(f"{letter} ", end="")
    print()

def print_hint(correct_word, word_length):
    found_positions = []
    for green_and_position in greens_and_positions:
        found_positions.append(int(green_and_position.split()[1]))

    for i in range(word_length):
        if i not in found_positions:
            print(f"Hint: letter {i+1} is {correct_word[i]}. For example, letter 3 in 'steak' is 'e'.")
            break


def find_word(words) -> list:
    """
    This function is set up as a series of eliminations whereby words, for example, that include
    letters that were previously eliminated, would be eliminated. It returns a list with all the possible
    words given the green yellow and eliminated letters.
    """
    # PSEUDOCODE FOR THE ELIMINATED SET
    # loop through all words in the list
    #     if none of the eliminated letters are in the word
    #         append the word to a shortlist

    # NOTE: You need to make sure that the loop takes into account all of the eliminated letters, some words slip through
    # if it counts one eliminated letter at a time.

    eliminated_shortlist = []
    for word in words:
        letters_in_word = 0
        for letter in eliminated:
            if letter in word:
                letters_in_word += 1
        if letters_in_word == 0:
            eliminated_shortlist.append(word)

    # PSEUDOCODE FOR THE YELLOWS SET
    # loop through all words in the eliminated shortlist (if its not empty)
    #     if all of the yellow letters are in the word and in the wrong position
    #         append the word to a shortlist

    yellows_shortlist = []
    if eliminated_shortlist:
        for word in eliminated_shortlist:
            letters_in_word_and_not_in_wrong_spot = 0
            for tmp in yellows_and_positions:
                letter, index = tmp.split()
                index = int(index)
                if letter != word[index] and letter in word:
                    letters_in_word_and_not_in_wrong_spot += 1
            if letters_in_word_and_not_in_wrong_spot == len(yellows_and_positions):
                yellows_shortlist.append(word)

    # PSEUDOCODE FOR THE GREENS SET
    # loop through all words in the yellows shortlist (if its not empty)
    #     if all of the greens letters are in the word and in the right position
    #         append the word to a shortlist

    greens_shortlist = []
    if yellows_shortlist:
        for word in yellows_shortlist:
            letters_in_word_and_right_spot = 0
            for tmp in greens_and_positions:
                letter, index = tmp.split()
                index = int(index)
                if letter == word[index]:
                    letters_in_word_and_right_spot += 1
            if letters_in_word_and_right_spot == len(greens_and_positions):
                greens_shortlist.append(word)

    return greens_shortlist



if __name__ == "__main__":
    main()
