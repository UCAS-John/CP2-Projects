import pandas as pd 
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coin_denomination.csv")

def load_coin_deno():
    return pd.read_csv(file_path)