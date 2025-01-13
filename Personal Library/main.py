#John Wangwang Personal Libary

"""
Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!
"""

def display(libary: list):
    pass

def add_items(libary: list, Title: str, Author: str, category: str):
    """
    
    """
    libary.append(dict())

def search(libary: list):
    pass

def remove_items(libary: list):
    pass

def main():

    libary = []

    print("In this program you will manage your own personal book libary!")

    while True:
        print("Select Action\n1. Display list\n2. Search list\n3. add book\n4. remove book")
        
        while True:
            try:
                action = int(input("Enter your action\n>>>"))
            except ValueError:
                print("Please enter an integer between 1-4")
                continue
            if action not in range(1,5):
                print("Please enter an integer between 1-4")
                continue
            break

        match action:
            case 1: 
                display(libary)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

if __name__ == "__main__":
    main()