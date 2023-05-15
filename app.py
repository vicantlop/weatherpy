import requests
import calendar
import json

print("type name of city and hit enter to get a 3 day forecast:")
city = input()

class Weather:
    def __init__(self, city):
        self.city = city
    
    def forecast(self):
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        querystring = {"q":f"{self.city}","days":"3"}

        headers = {
            "X-RapidAPI-Key": "187b0ec4b7msh9909e74c3e40f95p17b4b6jsn67ee1ffae374",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        formatted = json.dumps(data,indent=2)

        o = json.loads(formatted)

        location = o["location"]
        current = o["current"]
        forecast = o["forecast"]['forecastday']


        print(f'It is currently {current["temp_f"]} degrees fahrenheit and {current["condition"]["text"]} in {location["name"]}, {location["country"]}')

        count = 0

        for days in forecast:
            count += 1
            day = days["day"]
            print(f'{calendar.day_name[count]} will have a high of {day["maxtemp_f"]}, and a low of {day["mintemp_f"]}, and will be {day["condition"]["text"]}')

threeday = Weather(city)
threeday.forecast()


# location.name, .region, .country, .localtime
# current.temp_f, .condition.text
# forecast.forecastday[0], forecast.forecastday[0].maxtemp_f, forecast.forecastday[0].mintemp_f
# forecast.forecastday[1], forecast.forecastday[1].maxtemp_f, forecast.forecastday[1].mintemp_f, forecast.forecastday[1].condition.text