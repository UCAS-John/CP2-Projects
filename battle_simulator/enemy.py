from faker import Faker

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
    def gen_enemy():
        enemy_ls = []
        fake = Faker('en_US') 

        # Base enemy templates 
        enemy_templates = [
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 150, "strength": 16, "defense": 6, "speed": 3, "level": 5},
            {"name": "", "description": "", "health": 120, "strength": 18, "defense": 6, "speed": 5, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
        ]

        # Pick a random template and generate name and description
        for i in range(5):
            random_enemy = enemy_templates[i]
            random_enemy["name"] = fake.name()  # Random name
            random_enemy["description"] = f"{random_enemy['name']} was a {fake.job()} before turning evil in {fake.city()}."  

            # Create and return a Enemy instance
            enemy = Enemy(
                name=random_enemy["name"],
                description=random_enemy["description"],
                health=random_enemy["health"],
                strength=random_enemy["strength"],
                defense=random_enemy["defense"],
                speed=random_enemy["speed"],
                level=random_enemy["level"]
            )

            enemy_ls.append(enemy)

        return enemy_ls

    # Function to check if enemy in ls
    @staticmethod
    def check_enemy(name="", enemy_ls=[]):
        for enemy in enemy_ls:
            if enemy.name == name:
                return True
            
        return False
    
    def __str__(self):
        return (f"Enemy: {self.name}\n"
                f"Description: {self.description}")

if __name__ == "__main__":
    enemy_ls = Enemy.gen_enemy()
    for enemy in enemy_ls:
        print(enemy)