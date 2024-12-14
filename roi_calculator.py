# roi_calculator.py

# Function to convert American odds to Decimal odds
def american_to_decimal(american_odds):
    if american_odds > 0:
        return (american_odds / 100) + 1  # Positive odds
    else:
        return (100 / abs(american_odds)) + 1  # Negative odds

# Function to convert Decimal odds to American odds
def decimal_to_american(decimal_odds):
    if decimal_odds >= 2:
        return round((decimal_odds - 1) * 100)  # Positive odds
    else:
        return round(-100 / (decimal_odds - 1))  # Negative odds

# Function to apply profit boost to decimal odds
def apply_profit_boost(parlay_decimal_odds, profit_boost_input):
    if profit_boost_input > 0:
        profit_boost = profit_boost_input / 100  # Convert to percentage
        profit_portion = parlay_decimal_odds - 1  # Extract the profit portion
        boosted_profit = profit_portion * (1 + profit_boost)  # Apply the boost to the profit
        return 1 + boosted_profit  # Add back the original stake
    return parlay_decimal_odds

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

    return decimal_odds, parlay_american_odds

# Function to calculate ROI after profit boost
def calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage):
    implied_probability = 1 / original_decimal_odds
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)
    expected_return = vig_adjusted_probability * adjusted_decimal_odds * bet_amount
    roi_after_boost = (expected_return - bet_amount) / bet_amount * 100
    return roi_after_boost
