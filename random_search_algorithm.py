import random
# import time

# This is a variation of binary search which is used in computer guess
def algorithm(number, target, low, high):
    counter = 0
    while number != target:
        if number > target:
            high = number - 1
        elif number < target:
            low = number + 1
        counter += 1
        print(f"Number: {number}")
        # When executed with time.sleep, executing looks sick
        # time.sleep(0.01)
        number = random.randint(low, high)
    print(f"The target has been reached. {target}.")
    print(f"How long did it take to reach the target number? {counter}")
    
def main():
    low = 0
    high = 10 ** 100 # A googol is used as the example number on high
    target = random.randint(low, high)
    number = random.randint(low, high)
    while number == target:
        number = random.randint(low, high)
    number = 1
    print(f"Number: {number}")    
    print(f"Target: {target}")
    algorithm(number, target, low, high)

if __name__ == "__main__":
    main()
