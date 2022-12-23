"""
This module includes the functions for the following purposes:
- Checking if I or the user am one move away from winning
- Checking if I or the user has won or if its a tie
"""
def check_if_board_full(board):
    """
    Checks if the board is full, returns true if it is.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "e":
                return False
    return True

def check_win_user(board):
    """
    Checks if the user has won.
    """
    for i in range(3):
        if (board[i][0] == "o" and board[i][1] == "o" and board[i][2] == "o"):
            return True
    for i in range(3):
        if (board[0][i] == "o" and board[1][i] == "o" and board[2][i] == "o"):
            return True
    if (board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o"):
        return True
    if (board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o"):
        return True

def check_win_me(board):
    """
    Checks if I have won.
    """
    for i in range(3):
        if (board[i][0] == "x" and board[i][1] == "x" and board[i][2] == "x"):
            return True
    for i in range(3):
        if (board[0][i] == "x" and board[1][i] == "x" and board[2][i] == "x"):
            return True
    if (board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x"):
        return True
    if (board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x"):
        return True

def check_horizontal_left(board):
    """
    Checks each row, to see if there are two on the left side
    meaning that the user is about to win. If there are two on the left,
    it returns the third spot. In tictactoe this function is called,
    if it returns something, then place an x in the position it returned.
    The first number it returns is the row (zero indexed) and the second
    is the column. In tictactoe, I use .split() to get the separate values.
    """
    for i in range(3):
        match board[i]:
            case ["o", "o", "e"]:
                return f"{i} 2"

def check_horizontal_right(board):
    """
    Checks right side of rows.
    """
    for i in range(3):
        match board[i]:
            case ["e", "o", "o"]:
                return f"{i} 0"

def check_horizontal_middle(board):
    """
    Checks the middle of the rows.
    """
    for i in range(3):
        match board[i]:
            case ["o", "e", "o"]:
                return f"{i} 1"

def check_vertical_top(board):
    """
    With the way I have the board list set up, it's hard to check for vertical lines.
    So I'm setting a list "vertical" to make it similar to how it works above.
    Checks the top of columns.
    """
    vertical = [[board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]]]

    for i in range(3):
        match vertical[i]:
            case ["o", "o", "e"]:
                return f"2 {i}"

def check_vertical_bottom(board):
    """
    Checks the bottom of columns.
    """
    vertical = [[board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]]]

    for i in range(3):
        match vertical[i]:
            case ["e", "o", "o"]:
                return f"0 {i}"

def check_vertical_middle(board):
    """
    Checks the middle of columns.
    """
    vertical = [[board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]]]

    for i in range(3):
        match vertical[i]:
            case ["o", "e", "o"]:
                return f"1 {i}"

def check_cross(board):
    """
    Checks the diagonals.
    """
    cross_one = [board[0][0], board[1][1], board[2][2]]
    cross_two = [board[0][2], board[1][1], board[2][0]]

    match cross_one:
        case ["o", "o", "e"]:
            return "2 2"
        case ["e", "o", "o"]:
            return "0 0"
        case ["o", "e", "o"]:
            return "1 1"
    match cross_two:
        case ["o", "o", "e"]:
            return "2 0"
        case ["e", "o", "o"]:
            return "0 2"
        case ["o", "e", "o"]:
            return "1 1"

def check_about_to_win(board):
    """
    Instead of checking if the user is about to win,
    this checks if I'm about to win.
    Checks all rows, columns, and diagonals.
    """
    for i in range(3):
        match board[i]:
            case ["x", "x", "e"]:
                return f"{i} 2"
    for i in range(3):
        match board[i]:
            case ["e", "x", "x"]:
                return f"{i} 0"
    for i in range(3):
        match board[i]:
            case ["x", "e", "x"]:
                return f"{i} 1"
    vertical = [[board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]]]
    for i in range(3):
        match vertical[i]:
            case ["x", "x", "e"]:
                return f"2 {i}"
    for i in range(3):
        match vertical[i]:
            case ["e", "x", "x"]:
                return f"0 {i}"
    for i in range(3):
        match vertical[i]:
            case ["x", "e", "x"]:
                return f"1 {i}"
    cross_one = [board[0][0], board[1][1], board[2][2]]
    cross_two = [board[0][2], board[1][1], board[2][0]]
    match cross_one:
        case ["x", "x", "e"]:
            return "2 2"
        case ["e", "x", "x"]:
            return "0 0"
        case ["x", "e", "x"]:
            return "1 1"
    match cross_two:
        case ["x", "x", "e"]:
            return "2 0"
        case ["e", "x", "x"]:
            return "0 2"
        case ["x", "e", "x"]:
            return "1 1"

def check_if_about_to_win_or_lose(board):
    """
    Goes over all the other function, checks if the current
    game state is one move away from losing or winning. Returns
    the position to win, and avoid losing.

    I have to check if I'm about to win first or else if I'm
    one move from winning but the user is also one move away
    then instead of returning the move that will immediately
    win me the game, this will return the move that will block
    the user from winning.
    """
    if check_about_to_win(board):
        return check_about_to_win(board)
    if check_horizontal_left(board):
        return check_horizontal_left(board)
    if check_horizontal_right(board):
        return check_horizontal_right(board)
    if check_horizontal_middle(board):
        return check_horizontal_middle(board)
    if check_vertical_top(board):
        return check_vertical_top(board)
    if check_vertical_bottom(board):
        return check_vertical_bottom(board)
    if check_vertical_middle(board):
        return check_vertical_middle(board)
    if check_cross(board):
        return check_cross(board)
