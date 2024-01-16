// script.js
function getWeatherForecast() {
    var city = document.getElementById('cityInput').value;

    // Check if the city name is provided
    if (!city) {
        alert('Please enter a city name.');
        return;
    }

    // Call the backend to get forecast data and predictions
    fetch('/get_forecast', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `city=${encodeURIComponent(city)}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            displayForecastResults(data.forecast);
        }
    })
    .catch(error => {
        console.error('Error fetching forecast:', error);
        alert('Error fetching forecast. Please try again.');
    });
}

function displayForecastResults(predictions) {
    var forecastResults = document.getElementById('forecastResults');
    forecastResults.innerHTML = '';

    for (var date in predictions) {
        var card = document.createElement('div');
        card.className = `card ${getRainfallClass(predictions[date].rainfall)}`;
        card.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${getDayOfWeek(date)}</h5>
                <p class="card-text">${date}</p>
                <p class="card-text">Predicted Rainfall: ${getRainfallDescription(predictions[date].rainfall)}${' '}${predictions[date].actual_rainfall}${'mm'}</p>
                <p class="card-text">Temperature: ${predictions[date].temperature} &#8451;</p>
                <p class="card-text">Humidity: ${predictions[date].humidity}%</p>
                <p class="card-text">Wind Speed: ${predictions[date].wind_speed} m/s</p>
                <p class="card-text">Pressure: ${predictions[date].atmospheric_pressure} hPa</p>
            </div>
        `;

        forecastResults.appendChild(card);
    }
}

function getRainfallDescription(rainfall) {
    if (rainfall > 10) {
        return 'High Rainfall';
    } else if (rainfall > 5) {
        return 'Average Rainfall';
    } else {
        return 'No rainfall';
    }
}

function getDayOfWeek(dateString) {
    var daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var date = new Date(dateString);
    return daysOfWeek[date.getDay()];
}

function getRainfallClass(rainfall) {
    if (rainfall > 10) {
        return 'High rainfall';
    } else if (rainfall > 5) {
        return 'Average rainfall';
    } else {
        return 'Low rainfall';
    }
}
