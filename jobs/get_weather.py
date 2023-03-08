#!/usr/bin/env python

# import required modules
import requests, json
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Enter your API key here
api_key = os.getenv("API_KEY")
print(type(api_key))

# base_url variable to store url
base_url = BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=43.397221&lon=-80.311386&start=1675559598&end=1677978798"

# Give city name
city_name = "Lagos"


# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + str(api_key)

# get method of requests module
# return response object
response = requests.get(complete_url)
# HTTP request
info = []
coord_info = []
df = pd.DataFrame(columns=['dt', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3', 'aqi', 'lon', 'lat'])

# checking the status code of the request
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    for k, v in data.items():
        if k == 'coord':
            for a, t in v.items():
                coord_info.append(t)
        if k != 'coord':
            for f in v:
                info.append(f)
new_data = pd.DataFrame(info)
comp = pd.json_normalize(new_data['components'])
aqi = pd.json_normalize(new_data['main'])
new_data = pd.concat([new_data['dt'], comp, aqi], axis=1)
new_data[['lon', 'lat']] = coord_info
df = df.append(new_data, ignore_index=True)

new_data['dt'] = pd.to_datetime(new_data['dt'], unit='s')
print(new_data.head(20))