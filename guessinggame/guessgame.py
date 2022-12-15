from random import randrange



def main():

    level = get_level()

    print(f"I have a number between 0 and {level}, you're trying to find it.")

    right_number = randrange(level)



    # For example, if level is 1000 and right_number is 500, too_small would be 250 and too large would be 750. 
    # If level is 100, and right_number is 78, too_small would be 53 and too large would be 100. It would be 103 if it wasn't capped by the max() command.  
   

    too_small = max(right_number-round(level/4), 0)
    too_large = min(right_number+round(level/4), level)
    # print(f"Right number is {right_number} \nToo small is {too_small} \nToo large is {too_large}")

    while (True):

        guess = get_users_guess(level)
        
        if (right_number < guess < too_large):
            print("Too large!")
        elif (too_small < guess < right_number): 
            print("Too small!")
        elif (guess > too_large):
            print("Way too large!")
        elif (guess < too_small):
            print("Way too small!")
        elif (guess == right_number):
            print("Just right!")
            break

        

def get_level():
    n = 0
    while (n <= 0):
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
    return n

def get_users_guess(max_num):
    while (True):
        try:
            guess = int(input("Guess: "))
            if (guess <= 0 or guess > max_num):
                raise ValueError
            return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()