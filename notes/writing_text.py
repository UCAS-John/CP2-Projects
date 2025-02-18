import csv

# How do you find a file in a folder? 
# Copy file path

# In a python project how do you open a file?
# with open(file_path, "mode") as file:

# What is the difference between writing, appending, and creation modes?
"""
 Writing replace te old file
 Appending adds to the file
 Creating mode create file
"""

"""
r = to read the file
w = write on the file (replaces the old file)
w+ = read and write
a = append (adds to the file, doesn't delete them) (create a file if it doesn't exist)
x = create a file
a+ append and read
"""

# with open("text.txt", "a") as file:
#    file.write("happy\n")

data = [
    {"username": "ab", "color": "blue"},
    {"username": "cd", "color": "red"},
    {"username": "bjymt", "color": "yellow"},
    {"username": "wbaf", "color": "gray"},
    {"username": "ynersfdgf", "color": "cyan"},
    {"username": "gemsbf", "color": "black"},
    {"username": "tbasdfbwa", "color": "white"},
    {"username": "tnwatdad", "color": "dark blue"}
]

data.pop()

with open("user_info.csv", "w", newline="") as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("user_info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"username: {row[0]} \ncolor: {row[1]}")
        print("------------------------------------------")