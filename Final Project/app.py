from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from datetime import datetime, timedelta
import joblib


app = Flask(__name__, static_url_path='/static')

# Load the trained model
model_filename = 'random_forest_model.joblib'
model = joblib.load(model_filename)

# OpenWeather API key
api_key = '79b937b246a191044901c6a025a0131a'

# Function to process weather data and make predictions
def predict_rainfall(data):
    forecast = data['list']
    dates = [datetime.fromtimestamp(entry['dt']) for entry in forecast]
    temperatures = [entry['main']['temp'] - 273.15 for entry in forecast]
    humidities = [entry['main']['humidity'] for entry in forecast]
    winds = [entry['wind']['speed'] for entry in forecast]
    pressures = [entry['main']['pressure'] for entry in forecast]
    actual_rainfalls = [entry['rain']['3h'] if 'rain' in entry else 0 for entry in forecast]

    df = pd.DataFrame({
        'date': dates,
        'temp': temperatures,
        'hum': humidities,
        'wind': winds,
        'press': pressures,
    })

    # Make predictions using the trained model
    predictions = model.predict(df[['temp', 'hum', 'wind', 'press']])
    
    # Convert predictions to a dictionary for easier JSON serialization
    prediction_dict = {}
    for date, temp, hum, wind, press, actual_rainfall, prediction in zip(dates, temperatures, humidities, winds, pressures, actual_rainfalls, predictions):
        prediction_dict[date.strftime('%Y-%m-%d')] = {
            'rainfall': round(prediction, 2),
            'actual_rainfall': round(actual_rainfall, 2),
            'temperature': round(temp, 2),
            'humidity': hum,
            'wind_speed': wind,
            'atmospheric_pressure': press,
        }

    return prediction_dict

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_forecast', methods=['POST'])
def get_forecast():
    city = request.form['city']

    # Check if the city name is provided
    if not city:
        return jsonify({'error': 'Please enter a city name.'})

    # Call the OpenWeather API to get forecast data
    apiUrl = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    try:
        response = requests.get(apiUrl)
        data = response.json()
        if response.status_code != 200:
            return jsonify({'error': f'Error fetching weather data: {data["message"]}'})
    except Exception as e:
        return jsonify({'error': f'Error fetching weather data: {str(e)}'})

    # Process weather data and make predictions
    prediction_dict = predict_rainfall(data)
    return jsonify({'forecast': prediction_dict})

if __name__ == '__main__':
    app.run(debug=True)
