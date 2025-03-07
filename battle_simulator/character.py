import csv
import os

class Player:

    file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "character.csv")
    
    def __init__(self, name):
        
        self._created = False

        data = self.load_csv(name=name)
        
        if data:
            self.name = data["name"]
            self.health = data["health"]
            self.strength = data["strength"]
            self.defense = data["defense"]
            self.speed = data["speed"]
        else:
            self.name = name
            self.health = 0
            self.strength = 0
            self.defense = 0
            self.speed = 0
            self.save_csv()

        self.current_health = self.health        
       
    @staticmethod
    def load_csv(name: str, file_path=file_path) -> dict:

        data = {}

        try:
            with open(file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row.get("name", "") == name:
                        data = row
        except FileNotFoundError:
            print("Invalid file path")
        except Exception as e:
            print(f"Error loading file: {e}")

        return data

    def save_csv(self,file_path=file_path):
        try:
            data = Player.load_csv(name=self.name)

            fieldnames = ['name', 'health', 'strength', 'defense', 'speed']
            data = {
                   "name": self.name,
                   "health": self.health,
                   "strength": self.strength,
                   "defense": self.defense,
                   "speed": self.speed
                }

            with open(file_path, "w", newline="") as file:
               writer = csv.DictWriter(file, fieldnames=fieldnames)

               writer.writeheader()
               writer.writerow(data)
        except FileNotFoundError:
            print("Invalid file path")
        except Exception as e:
            print(f"Error saving file: {e}")

    def display_stat(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}") 
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")

    @staticmethod
    def check_character(name: str) -> bool:
        data = Player.load_csv(name)
        if data:
            return True
        else:
            return False
    
    @staticmethod
    def create_character(name: str):
        if Player.check_character(name):
            print(f"Chracter name: {name} already created")
            return None
        else:
            print(f"Create Chracter name: {name}")
            return Player(name)
    
    @staticmethod
    def login_charcter(name: str):
        if Player.check_character(name):
            return Player(name)
        else:
            print(f"Chracter name: {name} doesn't exist\nPlease Create Character first")
            return None

if __name__ == "__main__":
    choice = input(">>>")
    name = input("name: ")
    # match choice:
        #case '1':
            # player = login_charcter(name)
            # if not player:
            #   exit()
            # player.display_stat()
        # case '2':
            
            # player = create_character(name)
            # if not player:
            #    exit()
            #player.display_stat()
