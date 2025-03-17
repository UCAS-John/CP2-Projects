from character import Player
import random

def battle(character1: Player, character2: Player):
    print(f"\nBattle: {character1.name} vs {character2.name}")

    def calc_dmg(attacker: Player, defender: Player):
        damage:  float = attacker.strength - (defender.defense * 0.5)
        return damage

    def take_damage(receiver, damage):
        if receiver == 1:
            character1.current_health -= damage
        else:
            character2.current_health -= damage

    def dodge(receiver: Player, attacker: Player):
        if receiver.speed - attacker.speed <= 0:
            return False
        else:
            if random.random() < receiver.speed/100:
                return True
            else:
                return False
    
    def heal(character):
        if character == 1:
            character1.current_health += 10
        else:
            character2.current_health += 10
            
    skills = ['attack', 'heal']

    def get_skill_choice():
        for i, skill in enumerate(skills, start=1):
            print(f"{i}) {skill}")

        choice = input("Enter skill to use: ").strip()

        if choice not in ['1', '2']:
            print("\nInvalid Skill Choice\n")
            get_skill_choice()

        return choice

    choice = get_skill_choice()

    print("")
    match choice:
        case '1':
            damage = calc_dmg(attacker=character1, defender=character2)
            if dodge(attacker=character1, receiver=character2):
                print(f"{character1.name} miss the attack!")
            else:
                take_damage(receiver=2, damage=damage)
                print(f"{character2.name} recieve {damage} DMG and left with {character2.current_health} HP")

        case '2':
            print(f"{character1.name} healed up by 10")
            heal(character=1)

    if character2.current_health <= 0:
        print(f"{character1.name} won the battle")
        character1.gain_exp(130)
        return 1
    
    choice = random.randint(1,2)
    
    match choice:
        case 1:
            damage = calc_dmg(attacker=character2, defender=character1)
            if dodge(attacker=character2, receiver=character1):
                print(f"{character2.name} miss the attack!")
            else:
                take_damage(receiver=1, damage=damage)
                print(f"{character1.name} recieve {damage} DMG and left with {character1.current_health} HP")

        case 2:
            print(f"{character2.name} healed up by 10")
            heal(character=2)

    if character1.current_health <= 0:
        print(f"{character2.name} won the battle")
        character2.gain_exp(130)
        return 2
        
    battle(character1=character1, character2=character2)
        
if __name__ == "__main__":
    attack = Player("John")
    defender = Player("Nana")
    battle(attack, defender)
