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
from enemy import Enemy

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
            print("3) Display Analyzed Stat")
            print("4) logout")


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
        enemy_ls = Enemy.gen_enemy()
        choice = get_choice(logout=False)

        if not player:
            main()

        # Display List of Enemy and Get Enemy to fight
        def get_enemy():
            print("")
            for i, enemy in enumerate(enemy_ls, start=1):
                print(f"{i}) {enemy}")

            enemy = input("Enter character to to fight (index)\n>>> ").strip()

            if enemy not in ['1','2','3','4','5']:
                print("Invalid Chracter to fight")
                get_enemy()

            try:
                enemy = int(enemy)
            except:
                print("Must Enter integer")
                get_enemy()

            return enemy
        
        #function to start the battle
        def fight(player=player, enemy=None):
            battle(character1=player, enemy=enemy)
        
        match choice:
            case '1':
                enemy = get_enemy()
                enemy_class = enemy_ls[int(enemy)]

                fight(player=player, enemy=enemy_class)

                login()

            case '2':
                player.display_stat()
                login()

            case '3':
                player.display_analyzed_stats()
                login()

            case '4':
                main()

    login()

if __name__ ==  "__main__":
    main()
