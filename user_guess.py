import random
import sys

def handleUserInput():
    
    
    print()


def range():
    print("First of all, do you want to set the range in which the number is generated that you will need to guess?")
    range_q = input("Use y for yes, n for no (will default to 0 and 100) or e to exit (y/n/e): ")
    while True:
        if range_q == "y" or range_q == "Y":
            rangeLow = input("The lowest range number: ")
            while not rangeLow.isdigit():
                print("Again, please answer correctly with a number.")
                rangeLow = input("The lowest range number: ")

            rangeTop = input("The highest range number: ")
            while not rangeTop.isdigit():
                print("Again, please answer correctly with a number.")
                rangeTop = input("The highest range number: ")
            return [rangeLow, rangeTop]
        elif range_q == "n" or range_q == "N":
            return [0, 100]
        elif range_q == "e" or range_q == "E":
            sys.exit()
        else:
            print("Again, please answer correctly.")
            range_q = input("Use y for yes, n for no (will default to 0 and 100) or e to exit. (y/n/e): ")

def game(range_low, range_top):
    print(f"The number that you need to guess is generated in between {range_low} and {range_top}.\n")
    # User counter
    user_counter = 1
    # User number
    user_number = input(f"Your {user_counter}. number here: ")
    while not user_number.isdigit():
        print("Again, please answer correctly with a number.")
        user_number = input(f"Your {user_counter}. number here: ")
    user_number = int(user_number)

    # Random number from computer
    computer_number = random.randint(range_low, range_top)
    
    # Counter
    counter = 0
    print(f"Current counter: {counter}")
    
    # Main entry loop
    while user_number != computer_number:
        if user_number > computer_number: # You guessed too high
            print("You guessed too high. Guess lower.")
        else: # You guessed too low
            print("You guessed too low. Guess higher.")
        # User number
        user_number = input(f"Your {user_counter}. number here: ")
        while not user_number.isdigit():
            print("Again, please answer correctly with a number.")
            user_number = input(f"Your {user_counter}. number here: ")
        user_number = int(user_number)
        user_counter += 1
        counter += 1
        print(f"Current counter: {counter}")
    print(f"You correctly guessed the number {computer_number}!\nFinished!")

def main():
    print("Welcome to my guessing game!\nThe computer generates a random number and you will try to guess it.\nGood luck!\n")
    ranges = range()
    game(ranges[0], ranges[1])

if __name__ == "__main__":
    main()
