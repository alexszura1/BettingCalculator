# Function to convert American odds to Decimal odds
def american_to_decimal(american_odds):
    """Converts American odds to Decimal odds."""
    if american_odds > 0:
        return (american_odds / 100) + 1  # Positive odds
    else:
        return (100 / abs(american_odds)) + 1  # Negative odds


# Function to apply profit boost to decimal odds
def apply_profit_boost(parlay_decimal_odds, profit_boost_input):
    """Applies a profit boost to the given decimal odds."""
    if profit_boost_input != "0":
        profit_boost = float(profit_boost_input) / 100  # Convert to percentage (e.g., 50 -> 0.50)
        profit_portion = parlay_decimal_odds - 1  # Extract the profit portion
        boosted_profit = profit_portion * (1 + profit_boost)  # Apply the boost to the profit
        return 1 + boosted_profit  # Add back the original stake
    return parlay_decimal_odds


# Function to convert Decimal odds to American odds
def decimal_to_american(decimal_odds):
    """Converts Decimal odds to American odds."""
    if decimal_odds >= 2:
        return round((decimal_odds - 1) * 100)  # Positive odds
    else:
        return round(-100 / (decimal_odds - 1))  # Negative odds


# Collecting the number of legs in the parlay
num_legs = int(input("Enter the number of legs in the parlay: "))

# Collecting the odds for each leg
odds_list = []
for i in range(num_legs):
    odds = int(input(f"Enter the odds for leg {i+1} (e.g., -100 or 150): "))
    odds_list.append(odds)

# Calculating the total decimal odds for the parlay
decimal_odds = 1  # Initialize decimal odds
for odds in odds_list:
    decimal_odds *= american_to_decimal(odds)

# Collecting the profit boost input
profit_boost_input = input("Is there a profit boost? Enter the boost percentage (e.g., 10 for 10%) or 0 if none: ")

# Applying the profit boost to the decimal odds
adjusted_decimal_odds = apply_profit_boost(decimal_odds, profit_boost_input)

# Converting the adjusted decimal odds back to American odds
adjusted_parlay_american_odds = decimal_to_american(adjusted_decimal_odds)

# Output the results
print(f"\nTotal Decimal Odds before Boost: {decimal_odds:.2f}")
print(f"Total American Odds before Boost: {decimal_to_american(decimal_odds):.0f}")
print(f"Adjusted Decimal Odds with Profit Boost: {adjusted_decimal_odds:.2f}")
print(f"Adjusted American Odds with Profit Boost: {adjusted_parlay_american_odds:.0f}")


# Function to calculate ROI after applying profit boost
def calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage):
    """Calculates ROI after applying the profit boost to decimal odds."""
    print(f"\nAdjusted Decimal Odds with Profit Boost: {adjusted_decimal_odds:.2f}")
    print(f"Adjusted American Odds with Profit Boost: {decimal_to_american(adjusted_decimal_odds):.0f}")

    # Calculate implied probability from original decimal odds
    implied_probability = 1 / original_decimal_odds

    # Adjust implied probability for vig (market edge)
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)

    # Calculate the expected return using adjusted decimal odds
    expected_return = vig_adjusted_probability * adjusted_decimal_odds * bet_amount

    # Calculate ROI after applying the profit boost
    roi_after_boost = (expected_return - bet_amount) / bet_amount * 100
    print(f"ROI After Boost: {roi_after_boost:.2f}%")

    return roi_after_boost


# Example values for parlay calculations
original_decimal_odds = decimal_odds  # Total odds before profit boost
adjusted_decimal_odds = apply_profit_boost(decimal_odds, profit_boost_input)  # Adjusted decimal odds after profit boost
bet_amount = 100  # Bet amount (example)
vig_percentage = 4.76  # Vig or market edge percentage (example)

# Calculate ROI after applying profit boost
roi_after_boost = calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage)


# Function to calculate ROI before applying profit boost
def calculate_roi_before_boost_from_decimal(decimal_odds, bet_amount, vig_percentage):
    """Calculates ROI before applying any profit boost using decimal odds."""
    print(f"\nTotal Decimal Odds before Boost: {decimal_odds:.2f}")
    print(f"Total American Odds before Boost: {decimal_to_american(decimal_odds):.0f}")
    
    # Calculate implied probability from decimal odds
    implied_probability = 1 / decimal_odds

    # Adjust implied probability for vig
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)

    # Calculate expected return (expected value)
    expected_return = vig_adjusted_probability * decimal_odds * bet_amount

    # Calculate ROI before applying the boost
    roi_before_boost = (expected_return - bet_amount) / bet_amount * 100
    print(f"ROI Before Boost: {roi_before_boost:.2f}%")
    
    return roi_before_boost


# Calculate ROI before applying profit boost
roi_before_boost = calculate_roi_before_boost_from_decimal(decimal_odds, bet_amount, vig_percentage)
