def solve_coin_change(country, target, coin_data):

    def convert_to_cents(amount, denominations):
        # Convert amount to smallest unit
        target_cents = int(round(amount * 100))
        denoms_cents = {name: int(round(value * 100)) 
                        for name, value in denominations.items()}
        return target_cents, denoms_cents

    def coin_change(target_cents, denoms_cents):
        if target_cents < 0 or not denoms_cents:  # Return None if target amount is negative or no denominations
            return None, float('inf')
        if target_cents == 0:  # Return 0 if target amount is 0
            return {}, 0

        # Sort denominations by value in descending order 
        sorted_denoms = sorted(denoms_cents.items(), key=lambda x: x[1], reverse=True)

        coins_used = {}
        remaining_amount = target_cents

        for coin_name, coin_value in sorted_denoms:
            if coin_value <= remaining_amount:
                num_coins = remaining_amount // coin_value
                coins_used[coin_name] = num_coins
                remaining_amount %= coin_value

        # Return None if remaining amount is not zero
        if remaining_amount > 0:
            return None, float('inf')

        return coins_used, sum(coins_used.values())

    try:
        if country not in coin_data:
            raise ValueError(f"Country {country} not found!")
        
        denominations = coin_data[country]
        target_cents, denoms_cents = convert_to_cents(target, denominations)
        coins_used, min_coins = coin_change(target_cents, denoms_cents)
        
        # Check if a solution is possible
        if coins_used is None or min_coins >= float('inf'):
            return f"No solution possible for {target} using {country} coins!", None
        
        result = f"Minimum coins needed: {min_coins}\n"
        result += "Coins used:\n" + "\n".join(f"{coin_name}: {count}" for coin_name, count in coins_used.items())
        return result, min_coins
    
    except Exception as e:
        return str(e), None