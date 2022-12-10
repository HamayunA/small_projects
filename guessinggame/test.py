


def main():
    
    x = 10 
    global y
    y = 100
    z = 0

    match x:
        case 50:
            print("x is 50")
        case 90:
            print("x is 90")
        case other: 
            print("x is other")



if __name__ == "__main__":
    main()



