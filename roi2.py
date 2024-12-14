# Get the profit boost input from the user
profit_boost_input = input("Is there a profit boost? Enter the boost percentage (e.g., 10 for 10%) or 0 if none: ")

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
    if profit_boost_input != "0":
        profit_boost = float(profit_boost_input) / 100  # Convert to percentage (e.g., 50 -> 0.50)
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

# Get the number of legs in the parlay
num_legs = int(input("Enter the number of legs in the parlay: "))

# Collect the odds for each leg from the user
odds_list = []
for i in range(num_legs):
    odds = int(input(f"Enter the odds for leg {i+1} (e.g., -100 or 150): "))
    odds_list.append(odds)

# Calculate parlay odds
decimal_odds, parlay_american_odds = calculate_parlay(odds_list)

# Output the results
print(f"\nTotal Decimal Odds: {decimal_odds:.2f}")
print(f"Total American Odds: {parlay_american_odds}")


# Function to calculate ROI after profit boost using adjusted decimal odds
def calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage):
    # Print adjusted odds after applying the profit boost
    print(f"\nAdjusted Decimal Odds with Profit Boost: {adjusted_decimal_odds:.2f}")
    print(f"Adjusted American Odds with Profit Boost: {decimal_to_american(adjusted_decimal_odds):.0f}")

    # Use original decimal odds to compute implied probability
    implied_probability = 1 / original_decimal_odds

    # Adjust implied probability for vig
    vig_adjusted_probability = implied_probability / (1 + vig_percentage / 100)

    # Calculate expected return using the adjusted decimal odds
    expected_return = vig_adjusted_probability * adjusted_decimal_odds * bet_amount

    # Calculate ROI after boost
    roi_after_boost = (expected_return - bet_amount) / bet_amount * 100
    print(f"ROI After Boost: {roi_after_boost:.2f}%")

    return roi_after_boost


# Example Input from the earlier parlay calculations
original_decimal_odds = decimal_odds  # Total odds before profit boost
adjusted_decimal_odds = apply_profit_boost(decimal_odds, profit_boost_input)  # Adjusted decimal odds after profit boost
bet_amount = 100  # Bet amount
vig_percentage = 4.76  # Vig or market edge percentage

# Calculate ROI after profit boost
roi_after_boost = calculate_roi_after_boost(adjusted_decimal_odds, original_decimal_odds, bet_amount, vig_percentage)
