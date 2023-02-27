import requests
import json
import sys

def Process_Weather():
    
    CITY = 'Buenos Aires'
    API_KEY = '17a2808ca578d767dbb78b81bb10b171'
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}')
    r.raise_for_status()
    temp = {}

    args = sys.argv[1:]

    result = json.loads(r.text)
  
    for item in result:
        temp["City"] = result["name"]
        temp["Country"] = result["sys"]["country"]
        temp["Wind"] = result["wind"]["speed"]
        temp["Temperature"] = result["main"]["temp"]
        temp_temperature = temp["Temperature"]
        temp["Temperature"] = temp_temperature - 273.15
        temp["Humidity"] = result["main"]["humidity"]
        temp["Weather"] = result["weather"]
    

    print(temp)

Process_Weather()
