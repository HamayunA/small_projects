def get_word_length(word_length=1) -> int:
    """Asks user for a word length, returns an int between 3 and 15"""

    print("Your chosen length must be at least 3 and no more than 20. ")
    while word_length < 3 or word_length > 20:
        try:
            word_length = int(input("Word length: "))
        except ValueError:
            pass
    return word_length

def get_users_hint_preference():
    """Asks user if he or she prefers to play with hints. Returns false if not and true if so."""
    hints = "e"
    while hints != "y" and hints != "n":
        hints = input("Would you like hints(y/n)? ")

    if hints == "y":
        return True
    else:
        return False
    
def get_guess(words_of_specified_length, word_length) -> str:
    """
    Asks user for a guess, re-prompts if users guess is not of
    proper length, not alphabetical, or not in the dictionary.
    Returns the guess.
    """
    guess = "12345"
    while ((len(guess) != word_length) or (guess.isalpha() is False) or (guess not in words_of_specified_length)):
        guess = input("Guess: ")
    return guess

def get_words_of_specified_length(dictionary, word_length) -> list:
    """
    Reads the dictionary for words of user specified length,
    returns a list with all words of that length.
    """
    word_list = []
    for word in dictionary:
        if len(word) == word_length:
            word_list.append(word)
    return word_list


def get_dictionary() -> list:
    """Reads the words from the dictionary text file into a list and returns it"""
    dictionary = []
    with open("newdictionary.txt", "r") as file:
        for word in file.readlines():
            dictionary.append(word)
    dictionary = dictionary[0].split()
    return dictionary
