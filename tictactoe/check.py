


def main():
    pass
def check_win(board):
    # Horizontal, vertical, and diagonal
    for i in range(3):
        if (board[i][0] == "o" and board[i][1] == "o" and board[i][2] == "o"):
            return "user"
    for i in range(3):
        if (board[0][i] == "o" and board[1][i] == "o" and board[2][i] == "o"):
            return "user"
    if (board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o"):
        return "user"
    if (board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o"):
        return "user"

    for i in range(3):
        if (board[i][0] == "x" and board[i][1] == "x" and board[i][2] == "x"):
            return "me"
    for i in range(3):
        if (board[0][i] == "x" and board[1][i] == "x" and board[2][i] == "x"):
            return "me"
    if (board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x"):
        return "me"
    if (board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x"):
        return "me"

if __name__ == "__main__":
    main()