
b = True


def main():
    global b
    while (b):
        print("b is true")
        b = False
    

def foo():
    global b
    b = False

if __name__ == "__main__":
    main()
        