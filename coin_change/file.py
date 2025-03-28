import pandas as pd
from tkinter import messagebox

def load_coin_denominations(filename='coins.csv'):
    """Load and parse coin denominations from CSV file"""
    
    def read_csv_file(file_path):
        """Helper function to read CSV file"""
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found!")
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")
    
    def parse_coin_data(df):
        """Helper function to parse DataFrame into coin dictionary"""
        try:
            coin_dict = {}
            for country in df['Country'].unique():
                country_coins = df[df['Country'] == country]
                coin_dict[country] = {row['Name']: float(row['Value']) 
                                    for _, row in country_coins.iterrows()}
            return coin_dict
        except Exception as e:
            raise Exception(f"Error parsing coin data: {str(e)}")
    
    try:
        df = read_csv_file(filename)
        return parse_coin_data(df)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return {}
