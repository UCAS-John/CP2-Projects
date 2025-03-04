import csv
import os

def init_file():
    
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "character.csv")

    header = ['name', 'health', 'strength', 'defense', 'speed']
    
    try:
        with open(path,  "x") as file:
            writer = csv.writer(file)
            writer.writerow(header)
    except:
        return
