#!/usr/bin/env python3
# importing requests and json
import requests
import pandas as pd
import datetime

# base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=43.397221&lon=-80.311386&start=1675559598&end=1677978798"
# City Name
CITY = "Hyderabad"
# API key
API_KEY = "bc83258f0da0d1c1f4bdbf5b54261172"
# upadting the URL
URL = BASE_URL + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
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