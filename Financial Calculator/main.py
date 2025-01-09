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
    """
    Get amount of deposit in float
    Get the goal amount in float
    Get monthly as boolean to check if it weekly or monthly deposit
    return time in days
    """

    if monthly:
        time = math.ceil((goal/deposit)*30)
    else:
        time = math.ceil((goal/deposit)*7)

    return time 

def compound(balance: float, rate: float, year: int, time_per_year: int):
    """
    Get balance of current balance as float
    Get rate of interest rate as float
    Get year of how many years to calculate as integer
    Get tim_per_year as number of times interest is compounded per year as integer
    Return the amount of money after compounded
    """

    amount = balance*((1.0+(rate/time_per_year))**(time_per_year*year))
    return amount

def allocate(income: float):
    """
    Get income as a float data type
    Allocate
    20% to saving
    30% to entertainment
    50% to food
    Return dictionary of budget allocated
    """

    budget = {
        "Saving": 0,
        "Entertainment": 0,
        "Food": 0
    }

    budget["Saving"] = income * (20.0/100.0)
    budget["Entertainment"] = income * (30.0/100.0)
    budget["Food"] = income * (50.0/100.0)

    return budget

def sale_price(price:float, discount: float):
    """
    Get price and discount as float data type
    Return sale price
    """

    sale_price = price*((100.0-discount)/100.0)
    return sale_price

def tip(price: float, tip_percentage: float):
    """
    Get price and tip percentage as float
    Return how much tip you need to pay
    """

    tip = price*(tip_percentage/100)
    return tip

def main():

    instruction = """Choose the following calculator to calculate your financial
1. Amount of time to save for a goal based on a weekly or monthly deposit Calculator
2. Compound Interest Calculator 
3. Budget Allocator 
4. Sale Price Calculator 
5. Tip Calculator"""

    print(instruction)

    while True:
        try:
            choice = int(input("Type in number in integer to use Calculator: "))
        except ValueError:
            print("Please type in integer")
            continue
        
        if choice not in range(1,6):
            print("Please type in number between 1-5")
            continue
        else:
            break
    
    match choice:
        case 1:
            print("This is Amount of time to save for a goal based on a weekly or monthly deposit Calculator")

            while True:
                try:
                    deposit = float(input("Enter How much money you are going to deposit each time: "))
                    goal = float(input("Enter the amount of money you set as a goal: "))
                    decision = input("Weekly deposit or monthly deposit? (Type weekly or monthly): ")
                except ValueError:
                    print("Plese type in valid input!")
                    continue

                if decision == "weekly":
                    monthly = False
                    break
                elif decision == "monthly":
                    monthly = True
                    break
                else:
                    print("type in either weekly or monthly!")
                    continue
            
            days = saving_time(deposit, goal, monthly)
            print(f"You need {days} days to save up for ${goal} depositing {deposit} each time")

        case 2:
            print("This is Compound Interest Calculator")

            while True:
                try:
                    balance = float(input("Enter your current balance: "))
                    rate = float(input("Enter the interest rate: "))
                    time_per_year = int (input("Enter How many time your money is compound each year"))
                    year = int(input("Enter how many year your blance will compound: "))
                except ValueError:
                    print("Plese type in valid input!")
                    continue
                break

            compounded_balance = compound(balance, rate, year, time_per_year)
            print(f"After {year} years, you will have ${compounded_balance} in your balance")

        case 3:
            print("This is Budget Allocator")

            while True:
                try:
                    income = float(input("Enter your current income: "))
                except ValueError:
                    print("Plese type in valid input!")
                    continue
                break

            budget = allocate(income)
            print("This is your allocation with\n20% to saving\n30% to entertainment\n50% to food")
            for type in budget.keys():
                print(f"{type}: ${budget[type]}")

        case 4:
            print("This is Sale Price Calculator")

            while True:
                try:
                    price = float(input("Enter how much item cost: "))
                    sale_percentage = float(input("Enter how much your item is discount by %: "))
                except ValueError:
                    print("Plese type in valid input!")
                    continue
                break
            
            new_price = sale_price(price, sale_percentage)
            print(f"After apply {sale_percentage}% discount to ${price} item it now discounted to ${new_price}!")

        case 5:
            print("This is Tip Calculator")

            while True:
                try:
                    price = float(input("Enter how much services cost: "))
                    tip_percentage = float(input("Enter how much you want to tip by %: "))
                except ValueError:
                    print("Plese type in valid input!")
                    continue
                break

            tip_price = tip(price, tip_percentage)
            print(f"You have to pay ${tip_price} in tip!")

if __name__ == "__main__":
    main()