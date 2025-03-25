from character import Player
from enemy import Enemy
import random

def battle(character1: Player, enemy: Enemy):
    print(f"\nBattle: {character1.name} vs {enemy.name}")

    # Calculate damage that would be dealt
    def calc_dmg(attacker: Player, defender: Player):
        damage:  float = attacker.strength - (defender.defense * 0.5)
        return damage

    # Decrease health when chracter take damage
    def take_damage(receiver, damage):
        if receiver == 1:
            character1.current_health -= damage
        else:
            enemy.current_health -= damage

    # Calculate if character dodge the attack
    def dodge(receiver: Player, attacker: Player):
        if receiver.speed - attacker.speed <= 0:
            return False
        else:
            if random.random() < receiver.speed/100:
                return True
            else:
                return False
    
    # Increase Chracter Health
    def heal(character):
        if character == 1:
            character1.current_health += 10
        else:
            enemy.current_health += 10
            
    skills = ['attack', 'heal']

    # Get user input for which skill to use 
    def get_skill_choice():
        # Display all skills possible to use
        for i, skill in enumerate(skills, start=1):
            print(f"{i}) {skill}")

        choice = input("Enter skill to use: ").strip()

        # Check if input is valid
        if choice not in ['1', '2']:
            print("\nInvalid Skill Choice\n")
            get_skill_choice()

        return choice

    choice = get_skill_choice()

    print("")
    match choice:
        case '1':
            damage = calc_dmg(attacker=character1, defender=enemy)
            if dodge(attacker=character1, receiver=enemy):
                print(f"{character1.name} miss the attack!")
            else:
                take_damage(receiver=2, damage=damage)
                print(f"{enemy.name} recieve {damage} DMG and left with {enemy.current_health} HP")

        case '2':
            print(f"{character1.name} healed up by 10")
            heal(character=1)

    if enemy.current_health <= 0:
        print(f"{character1.name} won the battle")
        character1.gain_exp(130)
        return 1
    
    choice = random.randint(1,2) # Random enemy choice for heal or attack
    
    match choice:
        case 1:
            damage = calc_dmg(attacker=enemy, defender=character1)
            if dodge(attacker=enemy, receiver=character1):
                print(f"{enemy.name} miss the attack!")
            else:
                take_damage(receiver=1, damage=damage)
                print(f"{character1.name} recieve {damage} DMG and left with {character1.current_health} HP")

        case 2:
            print(f"{enemy.name} healed up by 10")
            heal(character=2)

    if character1.current_health <= 0:
        print(f"{enemy.name} won the battle")
        return 2
        
    battle(character1=character1, enemy=enemy)
        
if __name__ == "__main__":
    attack = Player("John")
    defender = Player("Nana")
    battle(attack, defender)
