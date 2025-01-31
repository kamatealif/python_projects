import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        if "data" in data:
            weather_data = {
                "city": city,
                "temperature": data["data"]["values"]["temperature"],
                "humidity": data["data"]["values"]["humidity"],
                "weather_code": data["data"]["values"]["weatherCode"]
            }
        else:
            weather_data = {"error": "City not found or API limit reached."}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)