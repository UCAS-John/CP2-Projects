#John Wangwang
import string

# Encode from english to morse code
def encode(english: list, morse: list, sentence: str):
    encoded = []
    
    for char in sentence:
        if char == " ": # Check for space
            encoded += "/"
        elif char in string.ascii_letters:  # Check if it is english letter
            # Find the corresponding morse code
            for alpha in english:
                if alpha == char.lower():
                    encoded.append(morse[english.index(alpha)]) # Access the corresponding letter in Morse Code
        else:
            return False  # Return False for non-letter characters

    return " ".join(encoded) # Join the encoded words with spaces between them

# Decode from morse code to english
def decode(english: list, morse: list, sentence: str):
    # Split the sentence by " / " 
    words = sentence.split(" / ")
    decoded = []

    for word in words:
        letters = word.split()  # Split word into letters
        decoded_word = ""

        for letter in letters:
            if letter in morse:  # Check if it is morse code character
                decoded_word += english[morse.index(letter)]  # Access the corresponding letter in English
            else:
                return False  # Return False for non-morse code character

        decoded.append(decoded_word)  # Add the decoded word to the list
    
    return " ".join(decoded)  # Join the decoded words with spaces between them

def main():
    
    # Define list of english letters and morse code letters
    english = list(string.ascii_lowercase)
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']


    while True:
        print("\nMorse Code Translator")

        print("1) Encode\n2) Decode\n3) Exit")

        choice  =  input(">>> ")

        match choice:
            # Encode
            case '1':
                    sentence = input("Enter your string\n>>> ")
                    morse_encoded = encode(english, morse, sentence)
                    if morse_encoded:
                        print(f"\nSentence : {sentence}\nMorse Code : {morse_encoded}")
                    else:
                        print("\nInvalid Input")
            # Decode
            case '2':
                    sentence = input("Enter your morse code\n>>> ")
                    string_decoded = decode(english, morse, sentence)
                    if string_decoded:
                        print(f"\nMorse Code : {sentence}\nSentence : {string_decoded}")
                    else:
                        print("\nInvalid Input")
            # Exit
            case '3':
                break
            # Handling un expected choice
            case _:
                  print("Please enter number between 1-3")
                  continue

if __name__ == "__main__":
    main()