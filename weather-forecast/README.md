# Weather Forecast CLI Tool

The **Weather Forecast CLI Tool** is a Python-based command-line application that allows users to fetch and display weather information for a specific city. It uses caching to minimize repeated API requests and enhance performance.

---

## Features

- **Fetch Weather Information:**  
  Get detailed weather information, including:
  - Temperature
  - Humidity
  - Wind Speed
  - Pressure
  - Visibility
  - Precipitation

- **Caching Mechanism:**  
  The tool caches weather data locally, reducing redundant API calls for previously queried cities.

- **Error Handling:**  
  Handles cases like:
  - Invalid city names
  - API errors (e.g., network issues or unavailability)

- **Astronomical Information:**  
  Displays sunrise and sunset times for the queried city.

---

## How It Works

1. **Menu Options:**  
   - `1`: Enter a city name to fetch its weather forecast.
   - `2`: Exit the application.

2. **Weather Data Retrieval:**  
   - If the city data exists in the cache, it is retrieved locally.
   - If not, the tool fetches the data from the `https://wttr.in/{city_name}?format=j1` API and stores it in the cache.

3. **Error Handling:**  
   - Detects invalid inputs (e.g., numbers or special characters in the city name).
   - Displays user-friendly error messages for API failures.

---

## How to Use

### Prerequisites

- Python 3.6 or later
- An active internet connection

### Steps

1. Clone the repository or download the script file.
2. Run the script:
   ```bash
   python <script_name>.py
3. Follow the prompts to fetch weather information.

### Example Output
```sh 
1. Enter the city name
2. Exit
Enter your choice: 1
Enter the city name: London
Fetching new data...
Weather Information:
---------------------
Location:
  Country: United Kingdom
  City: London
  Region: England

Current Weather:
  Temperature: 15°C
  Condition: Clear
  Humidity: 60%
  Wind: 10 Km/h
  Pressure: 1015 hPa
  Visibility: 10 km
  Precipitation: 0 mm

Astronomical Information:
  Sunrise: 07:45 AM
  Sunset: 04:30 PM

Last Updated: 03:15 PM
```
---
### Contributing
if you'd like to contribute:
1. Fork the Reposity.
2. Create a new branch.
3. Submit a pull request with your changes.