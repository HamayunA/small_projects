


def main():
    pass
def check_win_user(board):
    # Horizontal, vertical, and diagonal
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
    for i in range(3):
        match board[i]:
            case ["o", "o", "e"]:
                return f"{i} 2"
            case ["x", "x", "e"]:
                return f"{i} 2"
    
def check_horizontal_right(board):
    for i in range(3):
        match board[i]:
            case ["e", "o", "o"]:
                return f"{i} 0"
            case ["e", "x", "x"]:
                return f"{i} 0"

def check_vertical_top(board):
    # With the way I have the board list set up, it's hard to check for vertical lines. So I'm setting this up to make it similar to how it works above.
    vertical = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]

    # match vertical[0]:
    #     case ["o", "o", "e"]:
    #         return "2 0"
    # match vertical[1]:
    #     case ["o", "o", "e"]:
    #         return "2 1"
    # match vertical[2]:
    #     case ["o", "o", "e"]:
    #         return "2 2"

    for i in range(3):
        match vertical[i]:
            case ["o", "o", "e"]:
                return f"2 {i}"
            case ["x", "x", "e"]:
                return f"2 {i}"

def check_vertical_bottom(board):
    
    vertical = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]

    for i in range(3):
        match vertical[i]:
            case ["e", "o", "o"]:
                return f"0 {i}"
            case ["e", "x", "x"]:
                return f"0 {i}"
                
def check_cross(board):
    cross_one = [board[0][0], board[1][1], board[2][2]]
    cross_two = [board[0][2], board[1][1], board[2][0]]

    match cross_one:
        case ["o", "o", "e"]:
            return "2 2"
        case ["e", "o", "o"]:
            return "0 0"
        case ["x", "x", "e"]:
            return "2 2"
        case ["e", "x", "x"]:
            return "0 0"
    match cross_two:
        case ["o", "o", "e"]:
            return "2 0"
        case ["e", "o", "o"]:
            return "0 2"
        case ["x", "x", "e"]:
            return "2 0"
        case ["e", "x", "x"]:
            return "0 2"





if __name__ == "__main__":
    main()