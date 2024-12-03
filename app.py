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

    if request.method == 'POST':
        odds_list = request.form.getlist('odds[]')  # Retrieve odds as a list
        try:
            # Convert input strings to integers
            odds_list = [int(odds) for odds in odds_list]
            decimal_odds, american_odds = calculate_parlay(odds_list)
            results = {
                "decimal_odds": decimal_odds,
                "american_odds": american_odds
            }
        except ValueError:
            error_message = 'Please only input odds, i.e. -200, +150, etc.'

    return render_template('parlay.html', results=results, error_message=error_message)

@app.route('/profit_boost', methods=['GET', 'POST'])
def profit_boost():
    return render_template('profit_boost.html')

if __name__ == '__main__':
    app.run(debug=True)
