#John Wangwang Random Password Generator

"""
-A main function that runs the code
-Functions for the different password requirements
-A function that assembles that password once it is the correct length
-Users should be able to specify length and if they want to include
    -uppercase letters
    -lowercase letters
    -numbers
    -special characters
"""

import string
import random

# Add lowercase alphabet to random_char if user agree
def lower_case(random_char):

    while True:

        choice = input("Include lowercase letters in password (y/n)\n>>> ")

        if not choice.isalpha():
            print("\nPlease enter alphabet")
            continue
        elif choice.lower() not in ['y','n']:
            print("\nPlease enter letter 'y' for yes or 'n' for no")
            continue
        else:
            break
    
    if choice == 'n':
        return random_char
        
    random_char += string.ascii_lowercase

    return random_char

# Add uppercase alphabet to random_char if user agree
def upper_case(random_char):

    while True:

        choice = input("Include uppercase letters in password (y/n)\n>>> ")

        if not choice.isalpha():
            print("\nPlease enter alphabet")
            continue
        elif choice.lower() not in ['y','n']:
            print("\nPlease enter letter 'y' for yes or 'n' for no")
            continue
        else:
            break
    
    if choice == 'n':
        return random_char
        
    random_char += string.ascii_uppercase

    return random_char

# Add number to random_char if user agree
def digit(random_char):

    while True:

        choice = input("Include number in password (y/n)\n>>> ")

        if not choice.isalpha():
            print("\nPlease enter alphabet")
            continue
        elif choice.lower() not in ['y','n']:
            print("\nPlease enter letter 'y' for yes or 'n' for no")
            continue
        else:
            break
    
    if choice == 'n':
        return random_char
        
    random_char += string.digits 

    return random_char

# Add special character to random_char if user agree
def special_char(random_char):

    while True:

        choice = input("Include special letters in password (y/n)\n>>> ")

        if not choice.isalpha():
            print("\nPlease enter alphabet")
            continue
        elif choice.lower() not in ['y','n']:
            print("\nPlease enter letter 'y' for yes or 'n' for no")
            continue
        else:
            break
    
    if choice == 'n':
        return random_char
        
    random_char += string.punctuation

    return random_char

# Generate 4 passwords using random charcter in random_char with specific length
def generate_password(length: int, random_char):

    passwords = []

    for i in range(4):
        password = ""
        for j in range(length):
            password += random.choice(random_char)
        passwords.append(password)

    return passwords

def main():

    while True:

        print("\nRandom password generator\n")

        random_char = ""

        # Loop ask user for length of the password
        while True:
            try:
                length = int(input("Specify the length of your passowrd\n>>> "))
            except ValueError:
                print("Please specify the length using interger\n")
                continue
            if length < 0:
                print("Please Enter Positive Integer\n")
                continue
            else:
                break
        
        random_char = lower_case(random_char)
        random_char = upper_case(random_char)   
        random_char = digit(random_char)
        random_char = special_char(random_char)

        # Check if there is no character in random_char
        if not random_char:
            print("\nPlease select something!!!\n")
            choice = input("continue generatine password?\nPress 'n' to stop\n>>> ")
            if choice == 'n':
                break
            else:
                continue

        passwords = generate_password(length, random_char) # Genrate 4 password 

        # Print genrated password
        print("\nYour genrated password are")
        for password in passwords:
            print(f">>> {password}")

        # Check if user want to continue genrating password
        choice = input("\ncontinue generatine password?\nPress 'n' to stop\n>>> ") 
        if choice == 'n':
            break
        else:
            continue

if __name__ == "__main__":
    main()