document.getElementById('findWeather').addEventListener('click', function () {
	const date = document.getElementById('weatherDate').value
	if (date) {
		fetchWeather(date)
	} else {
		alert('Please enter a date.')
	}
})

function fetchWeather(date) {
	fetch(`/weather?date=${date}`)
		.then(response => response.json())
		.then(data => {
			displayWeather(data)
		})
		.catch(error => {
			console.error('Error fetching weather data:', error)
			document.getElementById('weatherInfo').innerText =
				'Error fetching weather data.'
		})
}

function displayWeather(data) {
	const weatherInfo = document.getElementById('weatherInfo')
	if (data.error) {
		weatherInfo.innerText = data.error
	} else {
		weatherInfo.innerHTML = `
            <p>Temperature: ${data.temperature}°C</p>
            <p>Condition: ${data.condition}</p>
            <p>Humidity: ${data.humidity}%</p>
        `
	}
}
