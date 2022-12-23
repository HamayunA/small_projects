



def main():
    user_going_first = ""
    while (user_going_first.lower() != "yes" and user_going_first.lower() != "no"):
        user_going_first = input("Would you like to go first? (yes or no) ").strip()

    print(user_going_first)
    if user_going_first.lower() == "yes":
        print("user_going_first is yes")

def foo():
    pass

if __name__ == "__main__":
    main()
                