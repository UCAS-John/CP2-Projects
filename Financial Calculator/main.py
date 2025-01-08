#John Wangwang Financial Calculator

"""
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
"""

import math

def saving_time(deposit: float, goal: float, monthly: bool):

    if monthly:
        time = math.ceil(goal/deposit)

    return time, monthly

def compound(balance: float, rate: float, year: float, time_per_year: int):

    amount = balance*((1.0+(rate/time_per_year))**(time_per_year*year))
    return amount

def allocate(income: float, ):
    pass
def sale_price(price:float, discount: float):

    sale_price = price*((100-discount)/100)
    return sale_price

def tip():
    pass

def main():
    pass

if __name__ == "__main__":
    main()