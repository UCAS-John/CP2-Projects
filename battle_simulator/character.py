import os
import matplotlib.pyplot as plt
import pandas as pd 

class Player:

    file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "character.csv") # Get file path base on chracter.py location

    def __init__(self, name):
        
        data = Player.load_csv(name=name)
        
        # Load chracter stat if chracter already exists
        if data is not None and not data.empty:
            self.name: str = data["name"].iloc[0]
            self.health: int = data["health"].iloc[0]
            self.strength: int = data["strength"].iloc[0]
            self.defense: int = data["defense"].iloc[0]
            self.speed: int = data["speed"].iloc[0]
            self.level: int = data["level"].iloc[0]
            self.exp: int = data["exp"].iloc[0]
        else:
            self.name = name
            self.health = 100
            self.strength = 20
            self.defense = 7
            self.speed = 5
            self.level = 1
            self.exp = 0
            self.save_csv()

        self.current_health = self.health        

    # Load Character stat
    # if all is set to True return list of dataframe of all character
    @staticmethod
    def load_csv(name="", file_path=file_path, all=False):
        df = pd.read_csv(filepath_or_buffer=file_path)
        if all:
            return df
        else:
            try:
                character = df.loc[df["name"] == name]
                return character
            except KeyError:
                return None
            except Exception as e:
                print(f"Error character loading: {e}")
                return None

    # save charcater stat to csv file
    def save_csv(self, file_path=file_path):
        try:
            data = Player.load_csv(all=True)
            info = {
                "name": self.name.lower(),
                "health": self.health,
                "strength": self.strength,
                "defense": self.defense,
                "speed": self.speed,
                "level": self.level,
                "exp": self.exp
            }

            names = data["name"].to_list()

            if self.name.lower() not in names:
                new_row = pd.DataFrame([info])
                data = pd.concat([data, new_row], ignore_index=True)
            else:
                data.loc[data["name"] == self.name.lower()] = pd.Series(info)
            data.to_csv(file_path, index=False)

        except Exception as e:
            print(f"Error saving character stat: {e}")

    # Display Character stat
    def display_stat(self):
        
        col = ["health", "strength", "defense", "speed", "level"]
        stat = [self.health, self.strength, self.defense, self.speed, self.level]

        plt.figure(figsize=(9, 3))
        plt.subplot(131)
        plt.bar(col, stat)
        plt.title(f"Stats for {self.name}")
        plt.show()

    # Character gain exp
    # If exp exceed 100 lv up by 1
    def gain_exp(self, exp = 0):

        current_exp = self.exp + exp
        if current_exp >= 100:
            gained_lv = int(current_exp/100)
            self.level += gained_lv
            self.exp = current_exp%100
            self.health += (gained_lv*14)
            self.strength += (gained_lv*4)
        else:
            self.exp += exp

        print(f"{self.name} just gained {exp} EXP!")
        self.save_csv()

    # Check if charcater exists if not exisits return false
    @staticmethod
    def check_character(name=""):
        name = name.lower()
            
        data = Player.load_csv(name)
        if data:
            return True
        else:
            return False

    # Function to crate character 
    # Return name 
    @staticmethod
    def create_character(name: str):
        if Player.check_character(name):
            print(f"Chracter name: {name} already created")
            return None
        else:
            print(f"Create Chracter name: {name}")
            return name

    # Function to login into character
    # Return name 
    @staticmethod
    def login_charcter(name: str):
        if Player.check_character(name):
            return name
        else:
            print(f"Chracter name: {name} doesn't exist\nPlease Create Character first")
            return None

if __name__ == "__main__":
    player = Player(name="john")
    player.display_stat()