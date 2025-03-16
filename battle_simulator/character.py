import csv
import os

class Player:

    file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "character.csv")
    enemy_list = ["Slime", "Zombie", "Skeleton"]

    def __init__(self, name):
        
        self._created = False

        data = Player.load_csv(name=name)
        
        if data:
            self.name: str = data["name"]
            self.health: int = data["health"]
            self.strength: int = data["strength"]
            self.defense: int = data["defense"]
            self.speed: int = data["speed"]
            self.level: int = data["level"]
            self.exp: int = data["exp"]
        else:
            self.name = name
            self.health = 100
            self.strength = 10
            self.defense = 7
            self.speed = 5
            self.level = 1
            self.exp = 0
            self.save_csv()

        self.current_health = self.health        

    @staticmethod
    def load_csv(name = None, file_path=file_path, all=False):
        
        data = None

        if all:
            try:
                data = []
                with open(file_path, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row.get("name", "") == name:
                            continue
                        data.append(row)
            except FileNotFoundError:
                print("Invalid file path")
            except Exception as e:
                print(f"Error loading file: {e}")
        else:
            try:
                data = {}
                with open(file_path, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row.get("name", "") == name:
                            data = row
                for stat in data:
                    if stat != 'name':
                        data[stat] = int(data[stat])

            except FileNotFoundError:
                print("Invalid file path")
            except Exception as e:
                print(f"Error loading file: {e}")

        return data

    def save_csv(self,file_path=file_path):
        try:
            data = Player.load_csv(name=self.name)

            fieldnames = ['name', 'health', 'strength', 'defense', 'speed', 'level', 'exp']
            data = {
                   "name": self.name,
                   "health": self.health,
                   "strength": self.strength,
                   "defense": self.defense,
                   "speed": self.speed,
                   "level": self.level,
                   "exp": self.exp
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
        print(f"Level: {self.level}")
        print(f"EXP: {self.exp}/100")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}") 
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")

    def gain_exp(self, exp: int):
        current_exp = self.exp + exp
        if current_exp >= 100:
            gained_lv = int(current_exp/100)
            self.level += gained_lv
            self.exp = current_exp%100
            self.health += (gained_lv*14)
            self.strength += (gained_lv*4)
        else:
            self.exp += exp
        self.save_csv()

    @staticmethod
    def check_character(name="", enemy_list=enemy_list):
        if name in enemy_list:
            return False
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
