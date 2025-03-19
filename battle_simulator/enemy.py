import csv
import os
import matplotlib.pyplot as plt
import pandas as pd 
import faker

class Enemy:

    file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "enemy.csv") # Get file path base on enemy.py location
    enemy_list = ["slime", "zombie", "skeleton"] # List of Default Enemy

    def __init__(self, name):
        
        data = Enemy.load_csv(name=name)
        
        self.name: str = data["name"]
        self.description: str = data["description"]
        self.health: int = data["health"]
        self.strength: int = data["strength"]
        self.defense: int = data["defense"]
        self.speed: int = data["speed"]
        self.level: int = data["level"]
        
        self.current_health = self.health        

    # Load Enemy Stat
    # Return dataframe of selected enemy
    @staticmethod
    def load_csv(name = None, file_path=file_path):
        
        data = None
        if name:
            name = name.lower()

        try:
            df = pd.read_csv(file_path)
            data = df.loc[df["name"] == name]
        except FileNotFoundError:
            print("Invalid file path")
        except Exception as e:
            print(f"Error loading file: {e}")

        return data
    
    @staticmethod
    def gen_enemy(number = 0):
        
        # name,health,strength,defense,speed,level,exp

        # slime,200,12,10,2,5,0
        # zombie,150,16,6,3,5,0
        # skeleton,120,18,6,5,5,0

        prebuilt_stat = [
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 150, "strength": 16, "defense": 6, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
            {"name": "", "description": "", "health": 200, "strength": 12, "defense": 10, "speed": 2, "level": 5},
        ]

        pass