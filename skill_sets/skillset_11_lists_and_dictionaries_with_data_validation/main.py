#!/usr/bin/env python3
import functions as f

def main():
    """Program entry. Calling environment to user-defined functions."""
    # initialize variables
    your_emails = [] # create empty list
    your_phones = [] # create empty list

    # function calls
    f.get_requirements()
    your_emails = f.add_emails()

    # use for testing return values
    # print(len(your_emails), your_emails)
    # exit()

    if len(your_emails) == 0:
        print("No emails!")
    else:
        your_phones = f.get_phones(your_emails)
        # testing returns
        # print(your_phones)
        # exit()
    
    contact_dict = f.create_contact(your_emails, your_phones) # original: f.create_contact(your_emails, your_phones)

    # add names
    f.add_contact_details(contact_dict)

    # update/delete
    while True:
        print("\nOptions:"
              + "\n(a) - Update contact"
              + "\n(b) - Delete contact"
              + "\n(c) - Show contact(s)"
              + "\n(-1) - Exit")
        option = input("Choose an options: ")
        if option == "a":
            f.update_contact(contact_dict)
        elif option == "b":
            f.delete_contact(contact_dict)
        elif option =="c":
            f.show_contacts(contact_dict)
        elif option =="-1":
            break
        else:
            print("Invalid option! Try again.")
        print("\nUpdated contact list: ")
        print(contact_dict)





# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# global variable, __name__, in module is entry point to program, that is, '__main__'. Otherwise, it's the name you import the module by.
# Code under if block will only run if module is entry point to your program.
# It allows code in module to be importable by other modules, without executing code block beneath on import.

# In short, use 'if __name__ == "main"' block to prevent (certain) code from being run when the module is imported.
# Put simply, __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.

# Executes main() function only if this file is executed as the main program.

if __name__=="__main__":
    main()