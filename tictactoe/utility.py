"""
Contains all functions that don't need to be in the
tictactoe module. For the sake of brevity.
"""
from random import randrange

def generate_random_spot():
    """
    Returns a randomly generated spot on the board.
    """
    row = randrange(0, 3)
    column = randrange(0, 3)
    return row, column

def print_board(board):
    """
    Prints the board.
    """
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("_________")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("_________")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("______________________________________________________")

def game_instructions():
    """
    Prints the game instructions for the user.
    """
    print("Type the row and column which you want to enter. E.G. 1 3  Your spots are circles.")

def empty_board():
    """
    Returns empty board. This is how the board is organized.
    """
    return [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]