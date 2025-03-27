from typing import Literal
import pandas as pd
from file import load_coin_deno

_COUNTRIES = Literal["USA", "Thailand", "Japan"]

def solve(country: _COUNTRIES, amount: float) -> pd.DataFrame:
    df = load_coin_deno(country)

    remaining_amount = amount

    for i in range(df.shape[0]):
        if remaining_amount == 0:
            break

        if i == 0:
            current_coin = df.iloc[df['Value'].idxmax()]
        else:
            current_coin = df.loc[df['Value'] == df['Value'].nlargest(i+1).iloc[-1]]
        
        coin_value = current_coin["Value"]
        coin_count = remaining_amount // coin_value
        remaining_amount = remaining_amount % coin_value

        df.loc[df['Name'] == current_coin['Name']]["Amount"] = coin_count

    return df

if __name__ == "__main__":
    df = solve("USA", 5.86)
    print(df.to_string())