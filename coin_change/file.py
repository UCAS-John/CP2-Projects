import pandas as pd 
from typing import Literal
import os

_COUNTRIES = Literal["USA", "Thailand", "Japan"]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coin_denomination.csv")

def load_coin_deno(country: _COUNTRIES):
    df = pd.read_csv(file_path)
    return df.loc[df["Country"] == country]

if __name__ == "__main__":
    df = load_coin_deno(country="USA")

    print(df.to_string)