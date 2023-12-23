import random
import time

def game():
    print("Welcome to my guessing game!\nYou set a number and your computer will try to guess it.\n")
    
    # User number
    user_number = input("Think about your number that your computer needs to guess (Just don't let it be over 2^63 - 1): ")
    while not user_number.isdigit():
        print("Again, please answer correctly with a number.")
        user_number = input("Think about your number: ")
    user_number = int(user_number)
    expo = len(str(user_number))
    high = 10 ** expo
    low = 0
    counter = 0

    # Random number
    random_number = random.randint(low, high)
    print(f"Computers guess: {random_number}")
    print(f"Current counter: {counter}")
    
    # Computer tries to guess the number
    while random_number != user_number:
        if random_number > user_number: # Computer guessed too high
            print("The computer guessed too high. It will guess lower.")
            high = random_number - 1
        elif random_number < user_number: # Computer guessed too low
            print("The computer guessed too low. It will guess higher.")
            low = random_number + 1
        # Generating new random number
        random_number = random.randint(low, high)
        
        counter += 1
        print(f"Computers guess: {random_number}")
        print(f"Current counter: {counter}")
        time.sleep(0.1)
    print(f"The number {random_number} was correctly guessed!\nFinished!")

def main():
    game()

if __name__ == "__main__":
    main()
