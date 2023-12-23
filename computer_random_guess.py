import random
import time
import sys

def range():
    print("First of all, do you want to set the range in which the number is generated that the computer will need to guess?")
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
    print()


def main(range_low, range):
    ranges = range()
    game()

if __name__ == "__main__":
    main()
