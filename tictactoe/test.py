



def main():
    board = [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]

    x = foo(board)
    foo(board)
    print(x)

def foo(b):
    match b:
        case [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]:
            return "0 0"

if __name__ == "__main__":
    main()
        