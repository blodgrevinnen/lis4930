#!/usr/bin/env python3
import functions as f

def main():
    """Program entry. Calling environment to user-defined functions."""
    # initialize variables
    low_num = 0
    high_num = 0

    #function cells
    f.get_requirements()
    low_num = f.get_lower()
    high_num = f.get_upper()

    # unit test
    # Note: in practice, test each function call individually!
    # print("\nPrinting lower num: ", low_num)
    # print("Printing higher num: ", high_num)
    # exit() # or, quit()

    while low_num > high_num:
        print("Lower number must be less than or equal to upper number! Try again!\n")
        low_num = f.get_lower()

    f.play_game(low_num, high_num)


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# global variable, __name__, in module is entry point to program, that is, '__main__'. Otherwise, it's the name you import the module by.
# Code under if block will only run if module is entry point to your program.
# It allows code in module to be importable by other modules, without executing code block beneath on import.

# In short, use 'if __name__ == "main"' block to prevent (certain) code from being run when the module is imported.
# Put simply, __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.

# Executes main() function only if this file is executed as the main program.

if __name__=="__main__":
    main()