import requests
import json
import argparse

def Process_Weather():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', help = 'please give a city', required= True)
    CITY = parser.parse_args()
    API_KEY = '17a2808ca578d767dbb78b81bb10b171'
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={CITY.city}&appid={API_KEY}')
    r.raise_for_status()
    temp = {}
    
    print(CITY)

    result = json.loads(r.text)
  
    for item in result:
        temp["City"] = result["name"]
        temp["Country"] = result["sys"]["country"]
        temp["Wind"] = result["wind"]["speed"]
        temp["Temperature"] = result["main"]["temp"]
        temp_temperature = temp["Temperature"]
        temp["Temperature"] = temp_temperature - 273.15
        temp["Humidity"] = result["main"]["humidity"]
        for item in result["weather"]:
            temp["Description"] = item["description"]
    

    print('--- Current Weather ---')
    print(f'City: {temp["City"]} | Country: {temp["Country"]}')
    print(f'Wind: {temp["Wind"]}   | Temperature: {temp["Temperature"]}')
    print(f'Humidity: {temp["Humidity"]} | Description: {temp["Description"]}')
    

Process_Weather()
