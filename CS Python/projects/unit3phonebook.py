# End of Unit 3: Telephone Book Project
#
# Purpose: To simulate a fully functioning 'address book'.
# Written as a Command Line Interface Program (text base)
# 1. Complete the code -alone- using the template below.
# 2. Do not 're-write' the project, make use of it.
# 3. Users are greeted with a welcome message and basic help
# 4. Users can gain access to help-menu by typing h/H/help.
#
# 5. Functionality of the program must be modular in design
# -  Each function must do useful work.
# -  The user must be protected from making basic errors
# -  User error must not crash the program
# -  The program must read the contact file into main memory
# -  The program must keep track of the changes made by the user
# -  The program must store the contact data before exiting
#
# 6. List of commands you must include:
# -  listAll(): a list of all addresses / contacts in the book
# -  listContacts(alpha): lists all contacts with a last name starting with 'alpha'
# -  findContact (person): looks for a given name and returns the contact details
# -  updateContact (person): replaces the contact in the address book with new info
# -  newContact(): creates a new contact in the address book
# -  deleteContact (person): removes the contact from the book perminently 
# -  quit(): saves all the contact data in a text file
#
# Author: Cole Becker
#
# Date: October 3 2023
#
# Setup the initial environment - import what you need to handle text-files
from os.path import exists
from colorama import Fore, Back, Style

# welcome message . . .
print("""\

 ____  _  _   __   __ _  ____  ____   __    __  __ _ 
(  _ \/ )( \ /  \ (  ( \(  __)(  _ \ /  \  /  \(  / )
 ) __/) __ ((  O )/    / ) _)  ) _ ((  O )(  O ))  ( 
(__)  \_)(_/ \__/ \_)__)(____)(____/ \__/  \__/(__\_)
""")

# Define Your Functions Here:

# create a new contact with five basic parts
def newContact():
    
    # input info for five basic parts
    firstName = input("please enter first name: ")
    lastName = input("please enter last name: ")
    phoneNumber = input("please enter phone number: ")
    address = input("please enter address: ")
    postalCode = input("please enter postalcode: ")
    
    # add all info to the different lists
    firstNlist.append(firstName)
    lastNlist.append(lastName)
    phoneList.append(phoneNumber)
    addressList.append(address)
    postalCodeList.append(postalCode)
    
    # let the user know it was succesfully created
    print(Fore.GREEN)
    print("contact succesfully added.")
    print(Fore.RESET)

# deletes a contact based on matching first and last name (assume unique)
def deleteContact(firstName, lastName):
    found = False #assume false unless find in contacts
    i = 0  # Initialize an index variable
    while i < len(firstNlist):
        if firstNlist[i].lower() == firstName.lower() and lastNlist[i].lower() == lastName.lower():
            del firstNlist[i]
            del lastNlist[i]
            del phoneList[i]
            del addressList[i]
            del postalCodeList[i]
            found = True
            print(Fore.GREEN)
            print("Contact successfully deleted.")
            print(Fore.RESET)
        else:
            i += 1
        if not found:
            print(Fore.RED)
            print("name not found in contacts...")
            print(Fore.RESET)

# takes in a first or last name, phone number or postal code
def findContact(searchContact):
    found = False
    for i in range(len(firstNlist)):
        if firstNlist[i].lower() == searchContact.lower() or lastNlist[i].lower() == searchContact.lower() or phoneList[i] == searchContact.lower() or addressList[i] == searchContact.lower() or postalCodeList[i] == searchContact.lower():
            print(Fore.BLUE + f"{firstNlist[i]}, {lastNlist[i]}, {phoneList[i]}, {addressList[i]}, {postalCodeList[i]}" + Fore.RESET)
            found = True
    
    if not found:
        print(Fore.RED)
        print("contact not found.")
        print(Fore.RESET)

# update contact
def updateContact(firstName, lastName):
    firstName = input("Enter the first name of the contact to update: ")
    lastName = input("Enter the last name of the contact to update: ")

    # Search for the contact in the lists
    index = -1  # start with invalid index
    for i in range(len(firstNlist)):
        if firstNlist[i].lower() == firstName.lower() and lastNlist[i].lower() == lastName.lower():
            index = i
            break
        
    if index != -1:
        # contact found ask for update
        new_firstName = input("Enter the new first name: ")
        new_lastName = input("Enter the new last name: ")
        new_phoneNumber = input("Enter the new phone number: ")
        new_address = input("Enter the new address: ")
        new_postalCode = input("Enter the new postal code: ")
        # update the list
        firstNlist[index] = new_firstName
        lastNlist[index] = new_lastName
        phoneList[index] = new_phoneNumber
        addressList[index] = new_address
        postalCodeList[index] = new_postalCode
        print(Fore.GREEN)
        print("contact succesfully updated.")
        print(Fore.RESET)
    else:
        print(Fore.RED)
        print("contact doesn't exist.")
        print(Fore.RESET)

# Continue creating useful functions below with your own criteria 
# save contacts when close
def saveContacts():
    with open("contacts.txt", "w") as file:
        for i in range(len(firstNlist)):
            file.write(f"{firstNlist[i]},{lastNlist[i]},{phoneList[i]},{addressList[i]},{postalCodeList[i]}\n")

# load contacts from file
def loadContacts():
    if exists("contacts.txt"): # if file exists it will add all info to the lists
        try:
            with open("contacts.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    firstName, lastName, phoneNumber, address, postalCode = line.strip().split(",")
                    firstNlist.append(firstName)
                    lastNlist.append(lastName)
                    phoneList.append(phoneNumber)
                    addressList.append(address)
                    postalCodeList.append(postalCode)
        except:
            print("error")
    else:
        print("no contact file saved we'll start fresh!") # will start with empty file if it can't find the file

# list all contacts
def listAll():
    if len(firstNlist) == 0:
        print("There are no contacts.")
    else:
        for i in range(len(firstNlist)):
            print(Fore.BLUE + f"{firstNlist[i]}, {lastNlist[i]}, {phoneList[i]}, {addressList[i]}, {postalCodeList[i]}" + Fore.RESET)

# list contacts with last name first letter
def listbylastName(alpha):
    for i in range(len(lastNlist)):
        if lastNlist[i][0].lower() == alpha.lower():
            print(Fore.BLUE + f"{firstNlist[i]}, {lastNlist[i]}, {phoneList[i]}, {addressList[i]}, {postalCodeList[i]}" + Fore.RESET)
        else:
            print(Fore.RED)
            print("contact not found")
            print(Fore.RESET)

# Memory Requirements - Global Variables (these lists must be used)
firstNlist = []       # These are parallel lists to store all user information.
lastNlist = []        # the firstNlist[0] corresponds to all the same user data
addressList = []      # found at element zero in the other lists. 
postalCodeList = []   # you must use these lists in your program as intended 
phoneList  = []

# add any other global variables you believe you need here . . 
loadContacts()

# MAIN PROGRAM LOOP - evaluating the data variable unil user (q)uits.
while True:
    data = input("Welcome .. for a list of commands type (h)elp or (q)uit: ")
    if data.lower() == 'q':
        saveContacts()
        print(Fore.GREEN + "saving contacts..." + Fore.RESET)
        break
    elif data.lower() == 'h':
        print("NC - create new contact")
        print("LA - lists all contacts")
        print("FC - find contact")
        print("DC - deletes contact")
        print("LB - list by start letter of last name")
        print("UP - update contact")
    elif data.lower() == 'nc':
        newContact()
    elif data.lower() == 'la':
        listAll()
    elif data.lower() == 'fc':
        searchContact = input("please enter a piece of information from the contact you are trying to find: ")
        findContact(searchContact)
    elif data.lower() == 'dc':
        firstName = input("please enter first name of the contact you wish to delete: ")
        lastName = input("please enter last name of the contact you wish to delete: ")
        deleteContact(firstName, lastName)
    elif data.lower() == 'lb':
        alpha = input("please enter one letter of the last name you want to sort by: ")
        listbylastName(alpha)
    elif data.lower() == 'up':
        firstName = ''
        lastName = ''
        updateContact(firstName, lastName)
    elif data.lower() == 'test':
        print(firstNlist)
        print(lastNlist)
    else:
        print(Fore.RED)
        print("error: invalid command.")
        print(Fore.RESET)


# NORMAL END PROGRAM
print("end of program . . .")