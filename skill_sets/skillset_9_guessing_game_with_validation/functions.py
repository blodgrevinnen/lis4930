#!/usr/bin/env python3
import random
"""

Defines four functions:

1. get_requirements
2. get_lower()
3. get_higher()
4. play_game()

"""

def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Tanner Morlan."
          + "\nGuessing Game!"
          + "\n\nProgram Requirements:"
          + "\n1. Create guessing game based on pseudo-random numbers."
          + "\n2. Must perform data and range validation."
          + "\n\n***Resource(s):***"
          + "\nGenerate pseudo-random numbers: https://docs.python.org/3/library/random.html"
          + "\n\nInput:")
    
# Input/Process/Output: IPO

def get_lower():
    """Accepts 0 args. Prompts for lower number, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            lower = 0 # could leave out this initialization

            # prompt lower number
            lower = int(input("Enter lower number: "))

            is_within_range = False
            while not is_within_range:
                if lower >= -1000 and lower <= 1000:
                    is_within_range = True
                else:
                    print("Lower must be between -1000 and 1000.\n")
                    lower = int(input("Enter lower: "))
            
        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return lower

def get_upper():
    """Accepts 0 args. Prompts for upper number, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            upper = 0 # could leave out this initialization

            # prompt upper number
            upper = int(input("Enter upper number: "))

            is_within_range = False
            while not is_within_range:
                if upper >= -1000 and upper <= 1000:
                    is_within_range = True
                else:
                    print("Upper must be between -1000 and 1000.\n")
                    upper = int(input("Enter upper: "))
                
        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return upper

def play_game(lower, upper):
    """Accepts 2 args. Creates pseudo-random number based upon user-entered values, and prompts user to guess."""
    # initialize variables
    count = 0
    rand_int = random.randint(lower, upper)

    while True:
        count += 1
        guess = int(input("\nEnter guess: "))

        if guess < rand_int:
            print("Too low!")
        elif guess > rand_int:
            print("Too high!")
        else:
            print("Bingo! Number of tries:", count)
            break