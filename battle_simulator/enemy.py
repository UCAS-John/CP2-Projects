from faker import Faker
import random

class Enemy:

    def __init__(self, name, description, health, strength, defense, speed, level):
        
        self.name: str = name 
        self.description: str = description
        self.health: int = health
        self.strength: int = strength
        self.defense: int = defense
        self.speed: int = speed
        self.level: int = level
        
        self.current_health = self.health        
    
    @staticmethod
    def gen_enemy(number = 0):

        fake = Faker('en_US') 

        enemies = [
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 150, "strength": 16, "defense": 6, "speed": 3, "level": 5},
            {"name": "", "description": "", "health": 120, "strength": 18, "defense": 6, "speed": 5, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
        ]

        for enemy in enemies:
            enemy["name"] = fake.name()
            enemy["description"] = fake.paragraph()

        print(enemies)

        random_enemy = random.choice(enemies)
        enemy = Enemy(
            name=random_enemy["name"],
            description=random_enemy["description"],
            health=random_enemy["health"],
            defense=random_enemy["defense"],
            speed=random_enemy["speed"],
            level=random_enemy["level"]
        )

        return enemy 

if __name__ == "__main__":
    Enemy.gen_enemy()