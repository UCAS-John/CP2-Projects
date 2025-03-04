import csv

def init_file():
   
    header = ['name', 'health', 'strength', 'defense', 'speed']
    
    try:
        with open("battle_simulator/character.csv", "x") as file:
            writer = csv.writer(file)
            writer.writerow(header)
    except:
        return
