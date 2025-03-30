import csv
from tkinter import messagebox
import os

# Load coin denominations
def load_coin_denominations(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)),'coins.csv')):
    
    def to_dict(rows):
        # change csv rows to dicitonary
        try:
            coin_dict = {}
            for row in rows:
                country = row[0]
                name = row[1]
                value = float(row[2])
                if country not in coin_dict:
                    coin_dict[country] = {}
                coin_dict[country][name] = value
            return coin_dict
        except Exception as e:
            raise Exception(f"Error changing coin data: {str(e)}")
    
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            # Read the rest of the rows into a list
            rows = list(reader)
        return to_dict(rows)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return {}
