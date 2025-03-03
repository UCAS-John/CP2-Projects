# John Wangwang, Advanced Functions Notes

# 1. What is a helper function?
    # A function written to be called in another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        # 8. What is recursion?
            # when you call a function inside of itself
        # 9. How does recursion work? 
        print("Please give me a number.")
        user_input = is_int(input("How old are you?\n"))
    else:
        return int(user_input)
    
def age():
    old = is_int(input("How old are you?\n"))
     
    print(f"Cool. You are {old}")

age()

# 2. What is the purpose of a helper function?
    # Helper function perform task that help other function
# 3. What is an inner function?
    # A function that is indisde of another function

# def add(a):
#     b = int(input("Give me a number"))

#     def addition():
#         print(a+b)
    
#     addition()

# add(3)

import logging

logging.basicConfig(level=logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

@logger
def adder(a, b):
    return a+b

# print(adder(3, 4))

# 4. What is the scope of a variable in a function WITH an inner function?
    # All variable that is outside and inside of an inner function
# 5. Why do we use inner functions?
    # So that inner function able to access all varaible of the outer function 
# 6. What is a closure function?
    # A closure function allows a function to remember value accross multiple calls

def add(a):
    b = int(input("Give me a number"))

    def addition():
        print(a+b)
    
    return addition

base = add(10)

# print(base(5))
# EXAMPLE

def math(income):

    def perc(amount, type):
        percent = amount/income 
        print(f"Your {type} is ${amount}, and that is {percent} of your income")
    
    return perc

def user_inputs(type):
    return int(input(f"What is your monthl {type}\n$"))

income = user_inputs("income")
rent = user_inputs("income")
utilities = user_inputs("income")
groceries = user_inputs("income")
transportation = user_inputs("income")

start = math()

# 7. Why do we write closure functions?
    # It remember value on multiple call