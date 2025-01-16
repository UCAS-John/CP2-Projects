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
    for (index, music_dict) in enumerate(libary):
        print(f"{index+1} | Title : {music_dict[0]}\n   | Author : {music_dict[1]}")

def add_items(libary: list, title: str, author: str):
    """
    
    """
    libary.append(tuple(title, author))

def search(libary: list, key: str):
    """
    
    """
    for music_dict in libary:
        for music in music_dict.values():
            if key in music:
                return music_dict

    print("We don't find what you are looking for")
    return False

def remove_items(libary: list, index: int):
    """
    
    """
    try:
        libary.remove(index)
    except KeyError:
        print("You remove non existance music")

    print(f"You remove {index} index book")

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

                while True:
                    try:
                        key = input("Serach >>> ")
                    except ValueError:
                        print("Please enter a keyword")
                        continue
                    break

                search(libary, key)

            case 3:
                pass
            case 4:
                pass

if __name__ == "__main__":
    main()