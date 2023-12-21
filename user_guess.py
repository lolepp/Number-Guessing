import random
import time

print("Welcome to my guessing game.\nThe computer generates a random number and you will try to guess it\nIf you end prematurely, just type anything unwanted.\nGood luck!")

range_q = input("First of all do you want to set the range of the numbers you need to guess.")

range = int(input("The highest number"))


user_counter = 1

user_number = int(input(f"Your {user_counter}. number here: "))

# Random number
random_number = random.randint(0, 1000)

counter = 0
print(f"Current counter: {counter}")

while user_number != random_number:
    if user_number > random_number: # You guessed too high
        print("You guessed too high. Guess lower.")


        user_number = int(input(f"Your {user_counter}. number here: "))
        
    else: # You guessed too low
        print("You guessed too low. Guess higher.")


        user_number = int(input(f"Your {user_counter}. number here: "))
        

    user_counter += 1
    counter += 1
    print(f"Current counter: {counter}")    
    time.sleep(0.1)


print("Correctly guessed!\nFinished!")


def main():
    print()

if __name__ == "__main__":
    main()
