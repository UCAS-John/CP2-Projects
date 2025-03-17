# John Wangwang Battle Simulator

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
import sys

from character import Player
from file import init_file
from battle import battle

def main():
    # initialize file
    init_file()
    
    print("Welcome to Battle Simulator")
    
    # Recursive get choice if choice is invalid
    def get_choice(logout=True):
        if logout:
            print("\n1) Create Character")
            print("2) Login Character")
            print("3) Exit")
        else:
            print("\n1) Battle")
            print("2) Display Stat")
            print("3) logout")


        choice = input(">>> ").strip()
        
        if choice not in ['1', '2', '3']: 
            get_choice()
        else:
            return choice

    choice = get_choice()

    # Get Character name
    def get_name():
        return input("Enter Chracter name: ").strip()
        
    match choice:
        case '1':
            name = get_name()
            name = Player.create_character(name)
            if name is None:
                main()
            player = Player(name=Player.create_character(name))
        case '2':
            name = get_name()
            name = Player.login_charcter(name)
            if name is None:
                main()
            player = Player(name=Player.login_charcter(name))
        case '3':
            sys.exit(0)
        case _:
            print("Invalid choice")
            main()
    
    if player is None:
        main()

    # Menu If Login
    def login():
        choice = get_choice(logout=False)

        if not player:
            main()

        # Display List of Enemy and Get Enemy to fight
        def get_enemy():
            data = Player.load_csv(name=player.name, all=True)
            print("")
            for i, enemy in enumerate(data, start=1):
                print(f"{i}) {enemy["name"]}")

            enemy = input("Enter character to to fight (Enter name)\n>>> ").strip().lower()

            if not Player.check_character(name=enemy, check_enemy=True):
                print("Invalid Chracter to fight")
                get_enemy()

            return enemy
        
        #function to start the battle
        def fight(player=player, enemy=None):
            battle(character1=player, character2=enemy)
        
        match choice:
            case '1':
                enemy = get_enemy()
                enemy_class = Player(name=enemy)

                fight(player=player, enemy=enemy_class)

                login()

            case '2':
                player.display_stat()
                login()

            case '3':
                main()

    login()

if __name__ ==  "__main__":
    main()
