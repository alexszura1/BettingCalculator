# roi_calculator.py

def american_to_decimal(american_odds):
    """Convert American odds to decimal odds."""
    if american_odds > 0:
        return (american_odds / 100) + 1
    else:
        return (100 / abs(american_odds)) + 1

def calculate_roi_before_boost(decimal_odds, bet_amount, vig_percentage):
    """Calculate ROI before boost (considering vig)."""
    vig_multiplier = (100 / (100 + vig_percentage))
    return ((decimal_odds - 1) * bet_amount) * vig_multiplier / bet_amount * 100

def calculate_roi_after_boost(adjusted_decimal_odds, decimal_odds, bet_amount, vig_percentage):
    """Calculate ROI after boost (considering vig)."""
    vig_multiplier = (100 / (100 + vig_percentage))
    boosted_payout = bet_amount * adjusted_decimal_odds
    original_payout = bet_amount * decimal_odds
    return ((boosted_payout - bet_amount) * vig_multiplier) / bet_amount * 100
