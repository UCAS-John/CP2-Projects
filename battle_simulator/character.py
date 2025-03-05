import csv
import os

class Player:
    def __init__(self, name):
        
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "character.csv")

        data = self.load_csv(name=name)
        
        if data:
            self.name = data["name"]
            self.health = data["health"]
            self.strength = data["strength"]
            self.defense = data["defense"]
            self.speed = data["speed"]
            self.level = data["level"] 
        else:
            self.name = name
            self.health = 100
            self.strength = 20
            self.defense = 10
            self.speed = 5
            self.level = 1
            self.save_csv()

    def load_csv(self, name: str):

        data = {}

        try:
            with open(self.path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("name", "") == name:
                        data = row
        except FileNotFoundError:
            print("Invalid file path")
        except Exception as e:
            print(f"Error loading file: {e}")
        
        return data

    def save_csv(self):
        try:
            data = self.load_csv(name=self.name)

            fieldnames = ['name', 'level', 'health', 'strength', 'defense', 'speed']
            data = {
                   "name": self.name,
                   "level": self.level,
                   "health": self.health,
                   "strength": self.strength,
                   "defense": self.defense,
                   "speed": self.speed,
                }

            with open(self.path, "w", newline="") as file:
               writer = csv.DictWriter(file, fieldnames=fieldnames)

               writer.writeheader()
               writer.writerow(data)
        except FileNotFoundError:
            print("Invalid file path")
        except Exception as e:
            print(f"Error saving file: {e}")

    def display_stat(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}") 
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        
