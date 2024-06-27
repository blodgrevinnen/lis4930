#!/usr/bin/env python3
import functions as f

def main():
    """Program entry. Calling environment to user-defined functions."""
    # initialize variables
    low_num = 0
    high_num = 0

    # create empty lists
    your_items = []
    your_costs = []

    # function calls
    f.get_requirements()
    your_items = f.add_items()

    # use for testing return values
    # print(len(your_items), your_items)
    # exit()

    if len(your_items) == 0:
        print("No shopping cart items.")
    else:
        your_costs = f.get_items_cost(your_items)
        # testing returns
        # print(your_costs)
        # exit()
        f.get_cart(your_items, your_costs)
        f.other_functionality(your_costs) # for extra credit



# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# global variable, __name__, in module is entry point to program, that is, '__main__'. Otherwise, it's the name you import the module by.
# Code under if block will only run if module is entry point to your program.
# It allows code in module to be importable by other modules, without executing code block beneath on import.

# In short, use 'if __name__ == "main"' block to prevent (certain) code from being run when the module is imported.
# Put simply, __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.

# Executes main() function only if this file is executed as the main program.

if __name__=="__main__":
    main()