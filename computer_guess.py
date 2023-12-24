import random
# import time

def get_user_number():
    # User number
    user_number = input("Think about your number that your computer needs to guess (Just don't let it be over 2^63 - 1): ")
    while not user_number.isdigit():
        print("Please enter a valid number.")
        user_number = input("Think about your number: ")
    return int(user_number)

def init_game(user_number):
    expo = len(str(user_number))
    high = 10 ** expo
    low = 0
    return low, high

def computer_guess(user_number, low, high):
    # Random number
    print(f"Now the computer tries to guess a number between {low} and {high}.\n")
    random_number = random.randint(low, high)
    counter = 0
    print(f"Computer's guess: {random_number}")
    print(f"Current counter: {counter}\n")
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

        print(f"Computer's guess: {random_number}")
        print(f"Current counter: {counter}\n")
        # time.sleep(0.001)
    print(f"The number {random_number} was correctly guessed!\nFinished.")
    print(f"How long did it take to reach the target number? {counter}")

def main():
    print("Welcome to my guessing game!\nYou set a number, and your computer will try to guess it.\n")
    user_number = get_user_number()
    low, high = init_game(user_number)
    computer_guess(user_number, low, high)

if __name__ == "__main__":
    main()
