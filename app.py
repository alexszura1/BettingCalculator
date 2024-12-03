from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parlay')
def parlay():
    return render_template('parlay.html')

@app.route('/profit_boost', methods=['GET', 'POST'])
def profit_boost():
    return render_template('profit_boost.html')

if __name__ == '__main__':
    app.run(debug=True)
