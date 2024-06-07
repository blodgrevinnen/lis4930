#!/usr/bin/env python3
"""
Defines five functions:
1. get_requirements()
2. get_list_size()
3. create_list()
4. get_sep_num()
5. get_list()

Define one extra credit function:
1. get_choice()
"""

def get_requirements():
    """Accepts 0 args. Displays program requirements and resources."""
    # header and requirements
    print("Developer: Tanner Morlan"
          + "\nWorking with lists and user-entered values."
          + "\n\nProgram Requirements:"
          + "\n1. Write program that prints all elements of user-entered list,"
          + "\n\tequal to and less than, or equal to and greater than user-entered value."
          + "\n2. Must perform data validation"
          + "\n3. ***Extra credit (10pts.):***"
          + "\n\tAllow user to choose equal to and less than, *or* equal to and greater than user-entered value."
          + "\n\n***Resource(s):***"
          + "\nLists: https://docs.python.org/3.12/tutorial/datastructures.html#more-on-lists"
          + "\n\nInput:")

def get_list_size():
    """Accepts 0 args. Prompts for list size, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            #initialize variable(s)
            size = 0 # could leave out this initialization

            # prompt user for list size
            size = int(input("Enter list size: "))

            is_within_range = False
            while not is_within_range:
                if size >= 1 and size <= 10:
                    is_within_range = True
                else:
                    print("List length must be between 1 and 10.\n")
                    size = int(input("Enter list size: "))
        
        except ValueError:
            print("Not and integer! Try again.\n")
            continue
        else:
            return size

def create_list(length):
    """Accepts 1 arg. Prompts user for list integers, based on list size. With data validation!"""
    # test valid int and w/in range
    # create empty list
    my_list = []

    while True:
        try:
            while len(my_list) < length:
                element = int(input("\nAdd number to list: "))
                my_list.append(element)
                print("Your number list: ", my_list)

        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return my_list
        
def get_sep_num():
    """Accepts 0 args. Prompts for separating number, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            number = 0 # could leave out this initialization
            
            # prompt user for separating integer
            number = int(input("\nEnter separating number: "))

        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return number

# extra credit function
def get_choice():
    """Accepts 0 args. Prompts user for equal to and less than *or* equal to and greater than user-entered value choice."""
    while True:
        choice = input("\nEnter '1' for less than or equal to, or '2' for greater than or equal to: ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Not a choice! Try again.\n")

def get_list(your_list, number, choice):
    """Accepts 3 args. Returns list of user-entered values based upon value entered and user choice."""
    # test separating integer against list
    if choice =='1':
        print("List numbers equal to and below separating number: ", [my_int for my_int in your_list if my_int <= number])
    else:
        print("List numbers equal to and above separating number: ", [my_int for my_int in your_list if my_int >= number])