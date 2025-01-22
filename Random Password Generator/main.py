#John Wangwang Random Password Generator

"""
-A main function that runs the code
-Functions for the different password requirements
-A function that assembles that password once it is the correct length
-Users should be able to specify length and if they want to include
    -uppercase letters
    -lowercase letters
    -numbers
    -special characters
"""
def generate_password(length: int, upper: bool, lower: bool, number: bool, special: bool):
    pass

def main():

    print("\nRandom password generator\n")

    while True:
        try:
            length = int(input("Specify the length of your passowrd\n>>> "))
        except ValueError:
            print("\nPlease specify the length using interger\n")
            continue
        if length < 0:
            print("\nPlease Enter Positive Integer\n")
            continue
        else:
            break
    
    choice = []
    for i in range(4):
        while True:
            if i == 0:
                choice[i] = input("Include uppercase letters in password (y/n)\n>>> ")
            elif i == 1:
                choice[i] = input("Include lowercase letters in password (y/n)\n>>> ")
            elif i == 2:
                choice[i] = input("Include number in password (y/n)\n>>> ")
            elif i == 3:
                choice[i] = input("Include special letters in password (y/n)\n>>> ")

            if not choice[i].isalpha():
                print("\nPlease enter alphabet\n")
                continue
            elif choice[i].lower() not in ['y','n']:
                print("\nPlease enter letter 'y' for yes or 'n' for no\n")
                continue
            else:
                break

    value = []
    for (index, char) in enumerate(choice):
        if char == "y":
            value[index] = True
        else:
            value[index] = False
    
    passwords = generate_password(length, value[0], value[1], value[2], value[3])

    print("Your genrated password are")
    for password in passwords:
        print(f">>> {password}")

if __name__ == "__main__":
    main()