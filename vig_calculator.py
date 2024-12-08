# Function to calculate implied probability from American odds
def implied_probability(american_odds):
    if american_odds > 0:
        return 100 / (american_odds + 100)
    else:
        return abs(american_odds) / (abs(american_odds) + 100)

# Function to calculate vig from two-sided market odds
def calculate_vig(odds_list):
    # Sum the implied probabilities for all outcomes
    total_implied_probability = sum(implied_probability(odds) for odds in odds_list)
    # Vig is the excess over 100%
    vig = total_implied_probability - 1  # Convert to percentage
    return vig * 100  # Return as percentage

# Example: Over/Under odds
over_under_odds = [-110, -110]

# Calculate vig
vig_percentage = calculate_vig(over_under_odds)
print(f"The vig for the market is: {vig_percentage:.2f}%")

