# Function to calculate ROI before boost using precomputed total decimal odds
def calculate_roi_before_boost_from_decimal(decimal_odds, bet_amount, vig_percentage):
    # Print total decimal odds and corresponding American odds before boost
    print(f"\nTotal Decimal Odds before Boost: {decimal_odds:.2f}")
    print(f"Total American Odds before Boost: {decimal_to_american(decimal_odds):.0f}")
    
    # Calculate the implied probability for the decimal odds
    implied_probability = 1 / decimal_odds  # For a single set of combined odds

    # Adjust implied probability for vig
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)

    # Calculate expected return (expected value)
    expected_return = vig_adjusted_probability * decimal_odds * bet_amount

    # Calculate ROI before boost
    roi_before_boost = (expected_return - bet_amount) / bet_amount * 100
    print(f"ROI Before Boost: {roi_before_boost:.2f}%")
    
    return roi_before_boost



# Calculate ROI before boost
roi_before_boost = calculate_roi_before_boost_from_decimal(decimal_odds, bet_amount, vig_percentage)
