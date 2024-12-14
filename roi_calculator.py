def calculate_roi(decimal_odds, bet_amount, vig_percentage):
    """Calculate the ROI based on decimal odds, bet amount, and vig percentage."""
    implied_probability = 1 / decimal_odds  # Calculate implied probability
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)  # Adjust for vig
    expected_return = vig_adjusted_probability * decimal_odds * bet_amount
    roi = (expected_return - bet_amount) / bet_amount * 100
    return roi

def calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage):
    """Calculate the ROI after applying a profit boost."""
    implied_probability = 1 / original_decimal_odds
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)
    expected_return = vig_adjusted_probability * adjusted_decimal_odds * bet_amount
    roi_after_boost = (expected_return - bet_amount) / bet_amount * 100
    return roi_after_boost

def american_to_decimal(american_odds):
    """Convert American odds to decimal odds."""
    if american_odds > 0:
        return 1 + (american_odds / 100)
    else:
        return 1 + (100 / abs(american_odds))

def decimal_to_american(decimal_odds):
    """Convert decimal odds to American odds."""
    if decimal_odds >= 2:
        return int((decimal_odds - 1) * 100)
    else:
        return int(-100 / (decimal_odds - 1))

def apply_profit_boost(decimal_odds, profit_boost_percentage):
    """Apply a profit boost to decimal odds."""
    return decimal_odds * (1 + profit_boost_percentage / 100)

def calculate_parlay_odds(odds_list):
    """Calculate the total decimal odds for a parlay given a list of individual leg odds."""
    decimal_odds = 1
    for odds in odds_list:
        decimal_odds *= american_to_decimal(odds)
    return decimal_odds

# Backend function to calculate all results
def calculate_parlay_results(odds_list, profit_boost_percentage, bet_amount, vig_percentage):
    """Calculate parlay results including ROI before and after a profit boost."""
    decimal_odds = calculate_parlay_odds(odds_list)
    adjusted_decimal_odds = apply_profit_boost(decimal_odds, profit_boost_percentage)

    roi_before_boost = calculate_roi(decimal_odds, bet_amount, vig_percentage)
    roi_after_boost = calculate_roi_after_boost(adjusted_decimal_odds, decimal_odds, bet_amount, vig_percentage)

    results = {
        "decimal_odds_before_boost": round(decimal_odds, 2),
        "american_odds_before_boost": decimal_to_american(decimal_odds),
        "decimal_odds_after_boost": round(adjusted_decimal_odds, 2),
        "american_odds_after_boost": decimal_to_american(adjusted_decimal_odds),
        "roi_before_boost": round(roi_before_boost, 2),
        "roi_after_boost": round(roi_after_boost, 2),
    }
    return results

# Example usage
odds_list = [100, 100]  # Example American odds for two legs
profit_boost_percentage = 50  # Example profit boost percentage
bet_amount = 100  # Example bet amount
vig_percentage = 4.76  # Example vig percentage

results = calculate_parlay_results(odds_list, profit_boost_percentage, bet_amount, vig_percentage)

# The results dictionary can be returned to the front end
print(results)
