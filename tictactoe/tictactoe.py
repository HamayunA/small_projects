from random import randrange
from check import check_win

def main():
    # Game instructions
    print("Your spots are marked with a circle. Type the row and column which you want to enter. E.G. 1 3  ")

    board = [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]

    for _ in range(8):

        print_board(board)

        row = 0
        column = 0
        while (board[row-1][column-1] == "x" or board[row-1][column-1] == "o" or (row > 3 or row < 1) or (column > 3 or column < 1)):
            row, column = input("Where: ").split()
            row = int(row)
            column = int(column)

        board[row-1][column-1] = "o"

        if (check_win(board) == "user"):
            print_board(board)
            print("You win this time...")
            break

        row, column = generate_random_spot()
        while (board[row][column] != "e"):
            row, column = generate_random_spot()

        board[row][column] = "x"

        if (check_win(board) == "me"):
            print_board(board)
            print("I win, suck it, loser!")
            break
        

def generate_random_spot():
    row = randrange(0, 3)
    column = randrange(0, 3)
    return row, column

def print_board(board):
    for i in range(len(board)):
            for j in range(len(board[i])):
                print(f"{board[i][j]} ", end="")
            print()

def check_if_board_full(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "e":
                return False
    return True
    
if __name__ == "__main__":
    main()