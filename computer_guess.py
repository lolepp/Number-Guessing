import random
import time

# Random number
random_number = random.randint(0, 1000)

# User number, if over 1000 it will be given the rest of the division of 1000 
user_number = int(input("Think about a number between 0 and 1000. ")) % 1000
print(user_number)

low = 0
high = 1000
counter = 0

print(f"Random number: {random_number}")
print(f"Current counter: {counter}")
# Computer tries to guess the number
while random_number != user_number:
    if random_number > user_number: # Computer guessed too high
        high = random_number
        # Generating new random number
        random_number = random.randint(low, random_number - 1)
        print(f"Random number: {random_number}")
    else: # Computer guessed too low
        low = random_number
        # Generating new random number
        random_number = random.randint(random_number + 1, high)
        print(f"Random number: {random_number}")
    counter += 1
    print(f"Current counter: {counter}")
    time.sleep(0.1)

print("Correctly guessed!\nFinished!")
