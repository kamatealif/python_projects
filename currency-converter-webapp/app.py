from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Free exchange rate API

@app.route("/", methods=["GET", "POST"])
def home():
    exchange_rates = requests.get(API_URL).json()["rates"]
    converted_amount = None

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = float(request.form["amount"])

        if from_currency in exchange_rates and to_currency in exchange_rates:
            converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])

    return render_template("index.html", rates=exchange_rates, converted_amount=converted_amount)

if __name__ == "__main__":
    app.run(debug=True)
