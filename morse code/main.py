#John Wangwang

def encode(string: str):
    return string

def decode(string: str):
    return string

def main():
        
    while True:
        print("Morse Code!!!")
        
        while True:

            print("1) Encode\n2) Decode")

            choice  =  input(">>> ")

            if choice not in ['1','2']:
                print("Please pick a number between 1 and 2")
                continue
            else:
                break

        match choice:
            case '1':
                    string = input("Enter your string\n>>> ")
                    morse_encoded = encode(string)
                    print(f"String : {string}\nMorse Code : {morse_encoded}")
            case '2':
                    morse = input("Enter your morse code\n>>> ")
                    string_decoded = encode(morse)
                    print(f"Morse Code : {morse}\nString : {string_decoded}")

        print("Do you wish to continue(Press 1 to stop)?")
        choice = input(">>> ")

        if choice == '1':
             break
        else:
             continue

if __name__ == "__main__":
    main()