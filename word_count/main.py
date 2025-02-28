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

from file import load
from timestamp import get_time

def main():
    print("Welcome to word counter")

    path = input("Enter path to your document file: ")

    data = load(path)

    if not data:
        ("Your document is empty")
        return

main()