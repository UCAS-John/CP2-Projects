def solve_coin_change(country, target, coin_data):

    def convert_to_cents(amount, denominations):
        # Convert amount to cents or equivalent smallest unit
        target_cents = int(round(amount * 100))
        denoms_cents = {name: int(round(value * 100)) 
                       for name, value in denominations.items()}
        return target_cents, denoms_cents
    
    def dp_coin_change(target_cents, denoms_cents):
        # Dynamic programming approach to find minimum coins
        if target_cents < 0 or not denoms_cents:
            return None, float('inf')
        if target_cents == 0:
            return [], 0

        coins_used = {}
        remaining_amount = target_cents

        for coin_name, coin_value in sorted(denoms_cents.items(), key=lambda x: x[1], reverse=True):
            if coin_value <= remaining_amount:
                num_coins = remaining_amount // coin_value
                coins_used[coin_name] = num_coins
                remaining_amount -= num_coins * coin_value

        if remaining_amount > 0:
            return None, float('inf')

        return coins_used, sum(coins_used.values())

    try:
        if country not in coin_data:
            raise ValueError(f"Country {country} not found!")
        
        denominations = coin_data[country]
        target_cents, denoms_cents = convert_to_cents(target, denominations)
        coins_used, min_coins = dp_coin_change(target_cents, denoms_cents)
        
        if coins_used is None:
            return f"No solution possible for {target} using {country} coins!", None
        
        result = f"Minimum coins needed: {min_coins}\n"
        result += "Coins used:\n" + "\n".join(f"{coin_name}: {count}" for coin_name, count in coins_used.items())
        return result, min_coins
    
    except Exception as e:
        return str(e), None