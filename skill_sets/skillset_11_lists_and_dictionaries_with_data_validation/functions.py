#!/usr/bin/env python3
"""
Defines five functions:

1. get_requirements()
2. add_emails()
3. get_phones()
4. create_contact()

Extra credit functions:
1. add_contact_details()
2. update_contact()
3. delete_contact()
"""

def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Tanner Morlan."
          + "\nWorking with lists, dictionaries, and user-entered values."
          + "\nProgram Requirements:"
          + "\n1. Write a program that prints all elements of a user-entered contact list."
          + "\n2. Must perform data validation."
          + "\n3. Dictionary key *must* be user's e-mail address."
          + "\n4. ***Extra credit (20pts. Both are optional.):***"
          + "\na) Provide additional functionality to add contacts' first and last names (10 pts)."
          + "\nb) Provide additional functionality to update *and* delete contacts (10 pts. Both required.)."
          + "\n\n**Resource(s):***"
          + "\nDictionaries:"
          + "\nhttps://www.codecademy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatcheet"
          + "\nhttps://www.pythoncheatsheet.org/cheatsheet/dictionaries"
          + "\n\nInput:")

def add_emails():
    """Accepts 0 args. Prompts for emails, returns user-entered values, including email count. With data validation!"""
    # test string input (can't be empty string!)

    print("Enter -1 to stop adding e-mails.\n")

    # initialize variable(s)
    email = ""
    count = 0
    my_emails = []

    # Note: -1 flag value
    while email != "-1":
        try:
            # prompt for email (Note: no newline, and counter variable to make "user-friendly.")
            print("{0}{1}{2}".format("Enter email ", count + 1, ": "), end="")

            email = input()
            # test for input(access first character, if none, error!)
            email[0]

            # stop loop with flag value
            if email == "-1":
                print("Stopping list!")
                break
            
            count += 1 # increment counter variable
            my_emails.append(email) # if all OK, append cart email

        except IndexError as e:
            # print(e) # only used for testing, to print generated error message
            print("No email entered! Try again.\n")
            continue
    
    # use for testing logic
    # print(count, my_emails)
    # exit()
    return my_emails

def get_phones(emails_list):
    """Accepts 1 arg. Prompts for phone numbers, based upon emails, returns user-entered values. With data validation!"""
    # test string input(can't be empty string!)

    #initialize variables
    phone = ""
    i = 0 # list email counter variable
    my_phones = [] # phone list

    for my_iterator in range(len(emails_list)):
        while True:
            try:
                # prompt for phone phones (Note: no newline, and counter variable to make "user-friendly.")
                # print("{0}{1}".format("phone", emails_list[i}]))
                print("\n{0}{1}".format(emails_list[i], ", phone:"))
                # or...
                # print("Enter phone number for " + str(emails_list[i]) + ":", end="")

                phone = input()

                # test for input (access first character, if none, error!)
                phone[0]

                i += 1 # increment list item variable
                my_phones.append(phone) # if all OK, append cart phone
                break

            except IndexError as e:
                # print(e) # only used to print generated error message
                print("No phone entered! Try again.")
                continue

    # use for testing logic
    # print(i, my_phones)
    # exit()
    return my_phones

def create_contact(keys, values):
    """Accepts 2 args. Creates dictionary based upon two list parameters. Displays dictionary elements."""
    my_dictionary = {} # create empty dictionary (Not really necessary here.)

    # Note: zip() function conjoins elements in two lists,; dict() converts resulting tuples into dictionary key-value pairs
    my_dictionary = dict(zip(keys, values))
    # testing returns
    # print(type(my_dictionary))
    # exit()

    """
    Following three functions returned through dictionary object:
    .keys() returns keys
    .values() returns values
    .items() returns both keys and values
    """

    print("\nPrinting dictionary:\n", my_dictionary)

    print("\nPrinting dictionary keys:\n", my_dictionary.keys())

    print("\nPrinting dictionary values:\n", my_dictionary.values())

    print("\nPrinting dictionary items:\n", my_dictionary.items())

    return my_dictionary

# extra credit functions

def add_contact_details(contact_dict):
    """Accepts 1 args. Adds first and last names to each contact in the dictionary."""
    for email in contact_dict:
        print(f"\nEnter details for {email}")
        first_name = input("FIrst name: ").strip()
        last_name = input("Last name: ").strip()
        contact_dict[email] = {
            "phone": contact_dict[email],
            "first_name": first_name,
            "last_name": last_name
        }

def update_contact(contact_dict):
    """Accepts 1 args. Updates the contact details for a given email."""
    email = input("Enter the email of the contact you want to update: ").strip()
    if email in contact_dict:
        print(f"\nUpdating details for {email}:")
        contact_dict[email]["phone"] = input("New phone: ").strip()
        contact_dict[email]["first_name"] = input("New first name: ").strip()
        contact_dict[email]["last_name"] = input ("New last name: ").strip()
    else:
        print("Contact not found.")

def delete_contact(contact_dict):
    """Accepts 1 args. Deletes a contact from the dictionary based on an email."""
    email = input("ENter the email of the contact you want to delete: ")
    if email in contact_dict:
        del contact_dict[email]
        print(f"Contact with email {email} has been deleted.")
    else:
        print("Contact not found.")

def show_contacts(contact_dict):
    """Displays all contacts in a user-friendly format."""
    if not contact_dict:
        print("No contacts to show.")
    else:
        print("\nContacts:")
        for email, details in contact_dict.items():
            print(f"\nEmail: {email}")
            print(f"Phone: {details['phone']}")
            print(f"First Name: {details['first_name']}")
            print(f"Last Name: {details['last_name']}")