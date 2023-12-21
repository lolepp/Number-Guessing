import random
import time
import sys

# def checkNumber(number):
    
#     print()

# def userNumber():
    
#     print()

def range():
    range_q = input("First of all, do you want to set the range of the numbers you need to guess. y for yes, n for no (will default to 0 and 100), e to exit (y/n/e/...) ")
    while True:
        if range_q == 'y' or 'Y':
            range_low = input("The lowest range number. ")
            range_top = input("The highest range number. ")
            while not range_low.isdigit() and not range_top.isdigit:
                range_low = input("Again, please answer correctly, with a number.\nThe lowest range number. ")
                range_top = input("Again, please answer correctly, with a number.\nThe highest range number. ")
            return (range_low, range_top)
        elif range_q == 'n' or 'N':
            return 0, 100
        elif range_q == 'e' or 'E':
            sys.exit()
        else:
            range_q = input("Again, please answer correctly, with a number\n. Use y or n. (y/n) ")

def game(range_low, range_top):
    print("Welcome to my guessing game.\nThe computer generates a random number and you will try to guess it\nIf you end prematurely, just type anything unwanted.\nGood luck!")
    user_counter = 1
    # User number
    user_number = int(input(f"Your {user_counter}. number here: ")) % range_top
    # Random number from computer
    random_number = random.randint(range_low, range_top)
    # Counter
    counter = 0
    print(f"Current counter: {counter}")
    # Main entry loop
    while user_number != random_number:
        if user_number > random_number: # You guessed too high
            print("You guessed too high. Guess lower.")
            # User number
            user_number = int(input(f"Your {user_counter}. number here: ")) % range_top
        else: # You guessed too low
            print("You guessed too low. Guess higher.")
            # User number
            user_number = int(input(f"Your {user_counter}. number here: ")) % range_top
        user_counter += 1
        counter += 1
        print(f"Current counter: {counter}")
        time.sleep(0.1)
    print("Correctly guessed!\nFinished!")

def main():
    x, y = range()
    game(x, y)

if __name__ == "__main__":
    main()
