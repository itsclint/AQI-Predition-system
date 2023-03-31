#!/usr/bin/env python3
import os
import requests
import pandas as pd

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

# Define the API endpoint and parameters
base_url = "http://api.openweathermap.org/data/2.5/air_pollution/history"
lat = "43.397221"
lon = "-80.311386"
start = "1675559598"
end = "1677978798"
api_key = os.getenv("API_KEY")


# Construct the URL with API key and parameters
url = f"{base_url}?lat={lat}&lon={lon}&start={start}&end={end}&appid={api_key}"

# Send HTTP request to OpenWeatherMap API
response = requests.get(url)

# Create empty list to hold response data
data = []

# Check the status code of the response
if response.status_code == 200:
    # Extract data from the response JSON
    response_json = response.json()
    for item in response_json["list"]:
        data.append({
            "dt": pd.to_datetime(item["dt"], unit="s"),
            "co": item["components"]["co"],
            "no": item["components"]["no"],
            "no2": item["components"]["no2"],
            "o3": item["components"]["o3"],
            "so2": item["components"]["so2"],
            "pm2_5": item["components"]["pm2_5"],
            "pm10": item["components"]["pm10"],
            "nh3": item["components"]["nh3"],
            "aqi": item["main"]["aqi"],
            "lon": response_json["coord"]["lon"],
            "lat": response_json["coord"]["lat"]
        })

    # Convert data list to pandas DataFrame
    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"HTTP request failed with status code {response.status_code}")