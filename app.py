from flask import Flask, render_template, request
from parlay_odds import calculate_parlay

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


@app.route('/profit_boost', methods=['GET', 'POST'])
def profit_boost():
    return render_template('profit_boost.html')

if __name__ == '__main__':
    app.run(debug=True)
