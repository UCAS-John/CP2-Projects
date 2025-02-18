#How do you find a file in a folder? 

#In a python project how do you open a file?
"""
r = to read the file
w = write on the file (replaces the old file)
w+ = read and write
a = append (adds to the file, doesn't delete them) (create a file if it doesn't exist)
x = create a file
a+ append and read
"""
with open("text.txt", "w") as file:
    file.write("U have change this file forever!")

#What is the difference between writing, appending, and creation modes?