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
from battle import battle

def main():
    init_file()
    
    print("Welcome to Battle Simulator")
    
    def get_choice():
        print("1) Create Character")
        print("2) Login Character")
        print("3) Exit")

        choice = input(">>> ")
        
        if choice not in ['1', '2', '3']: 
            get_choice()
        else:
            return choice

    choice = get_choice()

    def get_name():
        return input("Enter Chracter name: ")
        
    match choice:
        case '1':
            name = get_name()
            player = Player.create_character(name)
        case '2':
            name = get_name()
            player = Player.login_charcter(name)
        case '3':
            exit()
        case _:
            print("Invalid choice")
            main()

    if not player:
        main()

    def get_enemy():
        data = Player.load_csv(all=True)
        for i, enemy in enumerate(data):
            print(f"{i}) {enemy["name"]}")

        enemy = input("Enter character to to fight")

        if not Player.check_character(enemy):
            print("Invalid Chracter to fight")
            get_enemy()

        return enemy
    
    enemy = get_enemy()

    def fight():
        battle(character1=player, character2=enemy)

if __name__ ==  "__main__":
    main()
