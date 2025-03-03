"""
OVERVIEW:
Write a program that look at a document that a user has written on and update it with the word count and a timestamp for when that wordcount was last updated

REQUIREMENTS:
Uses at least 3 pages (main, file handling, and time handling) (main is the only file name I've given you)
Reads and Writes to the file
Uses functional decomposition
Lets the user tell what file to use it on
Uses good naming practices
Has good white space
"""

from file import process

def main():
    while True:
        print("\nDocument Word Counter")
        print("1) Update document with word count and timestamp")
        print("2) Exit")
        choice = input(">>> ")
        
        match choice:
            case '1':
                file_path = input("Enter the path to your document file: ")
                process(file_path)
            case '2':
                print("Exit")
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()