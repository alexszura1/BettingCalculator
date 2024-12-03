# parlay_odds.py

# Function to convert American odds to Decimal odds
def american_to_decimal(american_odds):
    if american_odds > 0:
        return (american_odds / 100) + 1  # Positive odds
    else:
        return (100 / abs(american_odds)) + 1  # Negative odds

# Function to calculate parlay odds
def calculate_parlay(odds_list):
    decimal_odds = 1  # Initialize decimal odds

    # Convert each leg's American odds to Decimal odds and multiply them
    for odds in odds_list:
        decimal_odds *= american_to_decimal(odds)

    # Convert back to American odds
    if decimal_odds > 2.00:
        parlay_american_odds = (decimal_odds - 1) * 100
    else:
        parlay_american_odds = -(100 / (decimal_odds - 1))

    return round(decimal_odds, 2), round(parlay_american_odds, 2)
