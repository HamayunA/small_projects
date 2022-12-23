from random import randrange
from check import check_win_me, check_win_user, check_horizontal_left, check_horizontal_right, check_vertical_bottom, check_vertical_top, check_cross


game_running = True


def main():
    game_instructions()
    board = empty_board()
    global game_running

    while (game_running):

        print_board(board)

        play_user_move(board)
        
        # I have to have check_if_I_win after play_my_move otherwise the computer plays a move even though it's won.
        check_user_wins(board)
        check_board_full(board)
        play_my_move(board)
        check_if_I_win(board)
        
        

        
        

def generate_random_spot():
    row = randrange(0, 3)
    column = randrange(0, 3)
    return row, column

def print_board(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("_________")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("_________")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    
def check_if_board_full(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "e":
                return False
    return True
    
def play_my_move(board):
    if (check_horizontal_left(board) != None):
        returned = check_horizontal_left(board)
        row, column = returned.split()
        board[int(row)][int(column)] = "x"
    elif (check_horizontal_right(board) != None):
        returned = check_horizontal_right(board)
        row, column = returned.split()
        board[int(row)][int(column)] = "x"
    elif (check_vertical_bottom(board) != None):
        returned = check_vertical_bottom(board)
        row, column = returned.split()
        board[int(row)][int(column)] = "x"
    elif (check_vertical_top(board) != None):
        returned = check_vertical_top(board)
        row, column = returned.split()
        board[int(row)][int(column)] = "x"
    elif (check_cross(board) != None):
        returned = check_cross(board)
        row, column = returned.split()
        board[int(row)][int(column)] = "x"
    else:
        row, column = generate_random_spot()
        while (board[row][column] != "e"):
            row, column = generate_random_spot()
        board[row][column] = "x"

def game_instructions():
    print("Your spots are marked with a circle. Type the row and column which you want to enter. E.G. 1 3  ")

def empty_board():
    return [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]

def check_user_wins(board):
    global game_running
    if (check_win_user(board)):
        print_board(board)
        print("You win this time...")
        game_running = False

def play_user_move(board):
    row = 0
    column = 0
    while (board[row-1][column-1] == "x" or board[row-1][column-1] == "o" or (row > 3 or row < 1) or (column > 3 or column < 1)):
        row, column = input("Where: ").split()
        row = int(row)
        column = int(column)
    board[row-1][column-1] = "o"

def check_board_full(board):
    global game_running
    if check_if_board_full(board):
        print_board(board)
        print("Looks like a tie.")
        game_running = False

def check_if_I_win(board):
    global game_running
    if (check_win_me(board)):
        print_board(board)
        print("I win, suck it, loser!")
        game_running = False

if __name__ == "__main__":
    main()