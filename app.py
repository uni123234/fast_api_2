from flask import Flask, render_template, request, jsonify
from flasgger import Swagger
import requests

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/")
def index():
    """
    Renders the index page.

    Returns:
        str: The rendered HTML for the index page.
    """
    return render_template("index.html")


@app.route("/weather", methods=["GET"])
def get_weather():
    """
    Weather API
    ---
    parameters:
      - name: date
        in: query
        type: string
        required: false
        description: The date for which weather is requested (format: YYYY-MM-DD)
    responses:
      200:
        description: A JSON object containing weather information
      404:
        description: Failed to fetch weather data
    """
    api_key = "YOUR_API_KEY"  # Замініть на ваш реальний API-ключ
    city_name = "CityName"  # Замініть на реальну назву міста

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    )

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(
            {
                "temperature": weather_data["main"]["temp"],
                "condition": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"],
            }
        )
    else:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
