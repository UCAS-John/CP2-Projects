def solve_coin_change(country, target, coin_data):
    """Solve Coin Change Problem with inner functions"""
    
    def convert_to_cents(amount, denominations):
        """Inner function to convert amounts to cents"""
        target_cents = int(round(amount * 100))
        denoms_cents = {name: int(round(value * 100)) 
                       for name, value in denominations.items()}
        return target_cents, denoms_cents
    
    def dp_coin_change(target_cents, denoms_cents):
        """Inner function implementing dynamic programming solution"""
        if target_cents < 0 or not denoms_cents:
            return None, float('inf')
        if target_cents == 0:
            return [], 0
            
        dp = [float('inf')] * (target_cents + 1)
        dp[0] = 0
        used_coins = [[] for _ in range(target_cents + 1)]
        
        for amount in range(1, target_cents + 1):
            for coin_name, coin_value in denoms_cents.items():
                if coin_value <= amount:
                    if dp[amount - coin_value] + 1 < dp[amount]:
                        dp[amount] = dp[amount - coin_value] + 1
                        used_coins[amount] = used_coins[amount - coin_value] + [coin_name]
        
        return used_coins[target_cents], dp[target_cents]
    
    try:
        if country not in coin_data:
            raise ValueError(f"Country {country} not found!")
        
        denominations = coin_data[country]
        target_cents, denoms_cents = convert_to_cents(target, denominations)
        coins_used, min_coins = dp_coin_change(target_cents, denoms_cents)
        
        if coins_used is None:
            return f"No solution possible for {target} using {country} coins!", None
        
        result = f"Minimum coins needed: {min_coins}\n"
        result += "Coins used: " + ", ".join(coins_used)
        return result, min_coins
    
    except Exception as e:
        return str(e), None