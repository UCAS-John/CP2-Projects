# John Wangwang, Multiple Python pages notes

# 1. How do you make multiple files in python?
    # Make a new file ending in .py
    # snake case file names
    # descriptive names (short)

# 2. How do you get a function from another file
# from calc import * (import everything)
from calc import addition as add, subtraction as sub # Alising is where you import a function and give it a new keyword
print(add())
print(sub(8, 0.5))

# 3. How do you get variables from another file?
from calc import NUM
# better to return a function

# 4. How do you have a function with multiple returns?
def get_uesr_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favourite color: ")
    return name, age ,color

name, age, color = get_uesr_info()

print(f"name: {name}\nage: {age}\ncolor: {color}")

# 5. Why would you use multiple pages for a python project? 
    # It is easier to merge github branch
    # Modularity = breaking the program into smaller more managable pieces
    # Functionality - Keeps your code clean