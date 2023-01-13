"""
A simple tic tac toe game.
Answer "yes" or "no" to the question if you want to go first.
To play a move at a specific location, specify the desired row, then column.
E.g.  "1 3" for row 1 and column 3.
"""
from random import randrange

from utility import generate_random_spot, print_board, game_instructions, empty_board
from check import check_win_me, check_win_user, check_if_about_to_win_or_lose, check_if_board_full



GAME_RUNNING = True

# Variable to count how many moves have been played, this will come in handy in play_my_move.
# It will help me figure out what moves are best if there neither me or the user are one
# Move away from winning
MOVE_COUNT = 0
# Check if user wants to go first
USER_GOING_FIRST = ""

while (USER_GOING_FIRST.lower() != "yes" and USER_GOING_FIRST.lower() != "no"):
    USER_GOING_FIRST = input("Would you like to go first? (yes or no) ").strip()

def main():
    """
    Main. Runs the game, calls other functions.
    """
    game_instructions()
    board = empty_board()
    global MOVE_COUNT



    if USER_GOING_FIRST == "yes":
        while GAME_RUNNING:
            print_board(board)
            play_user_move(board)
            MOVE_COUNT += 1
            check_user_wins(board)
            check_board_full(board)
            play_my_move(board)
            MOVE_COUNT += 1
            check_if_i_win(board)
    else:
        while GAME_RUNNING:
            play_my_move(board)
            MOVE_COUNT += 1
            print_board(board)

            check_if_i_win(board)

            check_board_full(board)

            if GAME_RUNNING:
                play_user_move(board)
                MOVE_COUNT += 1

            check_user_wins(board)


def play_my_move(board):
    """
    Runs algorithms to play the smartest move.
    """
    if USER_GOING_FIRST == "yes":
        if check_if_about_to_win_or_lose(board):
            returned = check_if_about_to_win_or_lose(board)
            row, column = returned.split()
            board[int(row)][int(column)] = "x"
        else:
            row, column = generate_random_spot()
            while board[row][column] != "e":
                row, column = generate_random_spot()
            board[row][column] = "x"
    else:
        if check_if_about_to_win_or_lose(board):
            returned = check_if_about_to_win_or_lose(board)
            row, column = returned.split()
            board[int(row)][int(column)] = "x"
        elif MOVE_COUNT == 0:
            board[0][0] = "x"
        #   if user plays opposite corner, play corner
        #        if user blocks my win, play corner
        #            win
        elif MOVE_COUNT == 2 and board[2][2] == "o":
            board[2][0] = "x"
        elif MOVE_COUNT == 4 and board[2][2] == "o" and board[1][0] == "o":
            board[0][2] = "x"
        #   if user plays corner beside, play opposite corner to me
        #       if user blocks my win, play corner
        #           win
        elif MOVE_COUNT == 2 and board[2][0] == "o":
            board[2][2] = "x"
        elif MOVE_COUNT == 4 and board[2][0] == "o" and board[1][1] == "o":
            board[0][2] = "x"
        elif MOVE_COUNT == 2 and board[0][2] == "o":
            board[2][2] = "x"
        elif MOVE_COUNT == 4 and board[0][2] == "o" and board[1][1] == "o":
            board[2][0] = "x"
        #   if user plays side beside, play middle
        #       if user blocks my win, play corner where user isnt blocking
        #           win
        elif MOVE_COUNT == 2 and board[0][1] == "o":
            board[1][1] = "x"
        elif MOVE_COUNT == 4 and board[0][1] == "o" and board[2][2] == "o":
            board[2][0] = "x"
        elif MOVE_COUNT == 2 and board[1][0] == "o":
            board[1][1] = "x"
        elif MOVE_COUNT == 4 and board[1][0] == "o" and board[2][2] == "o":
            board[0][2] = "x"
        #   if user plays side opposite, play middle
        #       if user blocks my win, block his win
        #           win
        elif MOVE_COUNT == 2 and (board[1][2] == "o" or board[2][1] == "o"):
            board[1][1] = "x"
        #   if user plays middle, play opposite corner
        #       if user plays corner, play corner
        #           win
        elif MOVE_COUNT == 2 and board[1][1] == "o":
            board[2][2] = "x"
        else:
            row, column = generate_random_spot()
            while board[row][column] != "e":
                row, column = generate_random_spot()
            board[row][column] = "x"





def check_user_wins(board):
    """
    Checks if the user has won, ends the game if so.
    """
    global GAME_RUNNING
    if check_win_user(board):
        print_board(board)
        print("You win this time...")
        GAME_RUNNING = False

def play_user_move(board):
    """
    Gets users move, when user inputs a valid move, it changes the board accordingly.
    """
    row = 0
    column = 0
    while (board[row-1][column-1] == "x" or board[row-1][column-1] == "o" or (row > 3 or row < 1) or (column > 3 or column < 1)):
        row, column = input("Where: ").split()
        row = int(row)
        column = int(column)
    board[row-1][column-1] = "o"

def check_board_full(board):
    """
    Checks if the board is full, ends the game if it is.
    """
    global GAME_RUNNING
    if check_if_board_full(board):
        print_board(board)
        print("Looks like a tie.")
        GAME_RUNNING = False

def check_if_i_win(board):
    """
    Checks if the computer has won, ends the game if it is.
    """
    global GAME_RUNNING
    if check_win_me(board):
        print_board(board)
        print("I win!")
        GAME_RUNNING = False

if __name__ == "__main__":
    main()
