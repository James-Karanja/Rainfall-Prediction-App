# Rainfall-Prediction-App
Web Application that predicts rainfall using a prediction model.


**Weather Prediction App**

Welcome to the Weather Prediction App repository! This project combines weather data from the OpenWeather API with a machine learning model to predict rainfall, temperature, humidity, wind speed, and atmospheric pressure for the next few days in a specified city. The predictions are displayed in a user-friendly web interface.


**Features:**

1. User-friendly Interface: Easily input a city name, and get detailed weather predictions with just a click.
Data Visualization: Results are displayed in a visually appealing card layout, providing insights into predicted rainfall, temperature, humidity, wind speed, and atmospheric pressure.

3. Machine Learning Integration: A trained machine learning model processes weather data to make accurate predictions for various weather parameters.
4. Responsive Design: Built with Bootstrap, the web interface is responsive and works seamlessly on both desktop and mobile devices.

**Technologies Used:**

1. Python: Backend server built with Flask to handle API requests and serve predictions.
2. Machine Learning: Utilizes a Random Forest model trained on weather data to make accurate predictions.
3. HTML/CSS/JavaScript: Frontend interface designed using Bootstrap for styling and JavaScript for dynamic functionality.
4. OpenWeather API: Retrieves current weather data and forecasts for a given city.

**Getting Started:**

1. Clone the repository.
2. Install the required Python packages using pip install -r requirements.txt.
3. Obtain an API key from OpenWeather and update the api_key variable in app.py.
4. Run the Flask app with python app.py.
5. Access the app at http://localhost:5000 in your browser.

Feel free to explore, contribute, and use this project to enhance your understanding of weather predictions!
