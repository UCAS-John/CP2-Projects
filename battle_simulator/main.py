"""
Character Creation and Management:

Create new characters with attributes (name, health, strength, defense, speed)
Save characters to a CSV file
Load characters from a CSV file
Display character information
Battle System:

Implement a turn-based battle system between two characters
Calculate damage based on character attributes
Include a simple leveling system where characters gain experience after battles
Program Structure:

Use inner functions for main features (character creation, battle system, menu)
Implement helper functions for repetitive tasks (save/load, display character info)
Create a main menu for user interaction
File Operations:

Save character data to a CSV file
Load character data from a CSV file
"""

from character import Player
from file import init_file

def main():
    init_file()
    
    print("Welcome to Battle Simulator")
    
    def get_choice():
        print("1) Create Character")
        print("2) Login Character")
        print("3) Exit")

        choice = input(">>> ")
        
        if choice not in ['1', '2']: 
            get_choice()
        else:
            return choice

    choice = get_choice()

    match choice:
        case '1':
            name = input("Enter Chracter name")
            Player(name)
        case '2':
            return

if __name__ ==  "__main__":
    main()
