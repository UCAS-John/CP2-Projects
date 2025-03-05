from character import Player
import random

def battle(character1: Player, character2: Player):
    print(f"\nBattle: {character1.name} vs {character2.name}")

    def calc_dmg(attacker: Player, defender: Player):
        damage:  float = attacker.strength - (defender.defense * 0.5)
        return damage

if __name__ == "__main__":
    attack = Player("John")
    defender = Player("Nana")
    battle(attack, defender)
