import requests
import calendar
from datetime import datetime
import json
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

class Weather:
    def __init__(self, city, days):
        self.city = city
        self.days = days
    
    def forecast(self):
        configure()
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        querystring = {"q":f"{self.city}","days":f"{self.days}"}

        headers = {
            "X-RapidAPI-Key": os.getenv('apikey'),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        formatted_data = json.dumps(data,indent=2)

        weatherObject = json.loads(formatted_data)

        location = weatherObject["location"]
        current = weatherObject["current"]
        forecast = weatherObject["forecast"]['forecastday']


        print(f'It is currently {current["temp_f"]} degrees fahrenheit and {current["condition"]["text"]} in {location["name"]}, {location["country"]}')

        dt = datetime.now()
        count = dt.weekday()

        for days in forecast:
            count += 1
            if count > 6:
                count -= 7
            day = days["day"]
            print(f'{calendar.day_name[count]} will have a high of {day["maxtemp_f"]}, and a low of {day["mintemp_f"]}, and will be {day["condition"]["text"]}')

def main():
    print("type name of city and hit enter:")
    city = input()
    print("Now please enter the number of days you would like a forecast for (please keep to 3 and under):")
    days = input()
    while int(days) > 3:
        print("Please enter a value of 3 or less:")
        days = input()

    userI = Weather(city, days)
    userI.forecast()

if __name__ == "__main__":
    main()


# location.name, .region, .country, .localtime
# current.temp_f, .condition.text
# forecast.forecastday[0], forecast.forecastday[0].maxtemp_f, forecast.forecastday[0].mintemp_f
# forecast.forecastday[1], forecast.forecastday[1].maxtemp_f, forecast.forecastday[1].mintemp_f, forecast.forecastday[1].condition.text
#changes