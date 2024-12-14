from flask import Flask, render_template, request
from parlay_odds import calculate_parlay
from roi_calculator import calculate_parlay_results  # Import the function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parlay', methods=['GET', 'POST'])
def parlay():
    error_message = None
    results = None
    dollar_amount = None
    payout = None

    if request.method == 'POST':
        try:
            # Retrieve the odds list as a list of integers
            odds_list = request.form.getlist('odds[]')
            odds_list = [int(odds) for odds in odds_list]

            # Calculate the parlay odds
            decimal_odds, american_odds = calculate_parlay(odds_list)

            # Get the dollar amount, if provided
            dollar_amount = request.form.get('dollar_amount')
            dollar_amount = float(dollar_amount) if dollar_amount else None

            # Calculate payout if a dollar amount is provided
            if dollar_amount:
                payout = dollar_amount * decimal_odds

            results = {
                "decimal_odds": round(decimal_odds, 2),
                "american_odds": round(american_odds),
                "payout": round(payout, 2) if payout else None
            }

        except ValueError:
            error_message = 'Please only input odds in the correct format (e.g., -200, +150, etc.).'

    return render_template('parlay.html', results=results, error_message=error_message, dollar_amount=dollar_amount)

@app.route('/roi_calculator', methods=['GET', 'POST'])
def roi_calculator():
    results = None
    error_message = None

    if request.method == 'POST':
        try:
            # Retrieve form inputs
            odds_list = [int(odds) for odds in request.form.getlist('odds[]')]
            profit_boost_percentage = float(request.form['profit_boost'])
            bet_amount = float(request.form['bet_amount'])
            vig_percentage = float(request.form['vig_percentage'])

            # Calculate results using the backend function
            results = calculate_parlay_results(
                odds_list, profit_boost_percentage, bet_amount, vig_percentage
            )

        except Exception as e:
            error_message = f"An error occurred: {e}"

    # Pass the results and any error message to the template
    return render_template('roi_calculator.html', results=results, error_message=error_message)

@app.route('/vig_calculator', methods=['GET', 'POST'])
def vig_calculator():
    def implied_probability(american_odds):
        if american_odds > 0:
            return 100 / (american_odds + 100)
        else:
            return abs(american_odds) / (abs(american_odds) + 100)

    def calculate_vig(odds_list):
        total_implied_probability = sum(implied_probability(odds) for odds in odds_list if odds != '')
        vig = total_implied_probability - 1
        return vig * 100

    if request.method == 'POST':
        # Collect odds from form
        odds1 = request.form.get('odds1')
        odds2 = request.form.get('odds2')
        odds3 = request.form.get('odds3')

        # Create a list of provided odds (filter empty inputs)
        odds_list = [int(odds) for odds in [odds1, odds2, odds3] if odds]

        # Calculate vig
        vig_percentage = round(calculate_vig(odds_list), 2)

        return render_template(
            'vig.html',
            vig=vig_percentage,
            odds_list=odds_list
        )

    # GET request: Render the form
    return render_template('vig.html', vig=None)


if __name__ == "__main__":
    app.run(debug=True)