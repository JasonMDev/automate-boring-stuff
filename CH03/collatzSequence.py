#! /usr/bin/python3
# This is a programme that shows off the collatz sequence.

# Determine collatz sequence
def collatz(anyNumber):
    if anyNumber % 2 == 0:
        # Even
        return anyNumber // 2
    elif anyNumber % 2 == 1:
        # Odd
        return 3 * anyNumber + 1

# Check if user value is a valid integer number.
# Will request untill true
def userInput():
    while True:    
        try:
            return int(input())
            break
        except ValueError:
            print('Error: Number not a valid integer number.')
            print('Please select a valid integer number...')


# Ask the player to guess a number.
print('Please select any number...')
myNumber = userInput()
while myNumber != 1:
    myNumber = collatz(myNumber)
    print(myNumber)

