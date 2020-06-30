# app/weather_service.py

import os
import csv
import json
from pprint import pprint
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from datetime import date
#from app.email_service import send_email

import requests
from dotenv import load_dotenv

from app import APP_ENV

load_dotenv()

csv_filepath = os.path.join(os.path.dirname(__file__), "Trail Park Database - Parks.csv")

with open(csv_filepath, "r") as csv_file:
    parks = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        parks.append(row)

print("-----------------------------")
print("Hey Happy Hiker!")
print("-----------------------------")
print("Please select from the list below: ")
print("-----------------------------")

original = []
for z in parks:
    print(z["park"])

print("-----------------------------")

destination = []
while True:
    park_id = input("Please Input Your Park to Start Your Adventure: ")

    if [p for p in parks if str(p["park"]) == park_id]:
        destination.append(park_id)
        break
    else:
        print("We don't play there! Please Re-Enter.")

for park_id in destination:
    matching_locations = [i for i in parks if str(i["park"]) == str(park_id)]
    matching_location = matching_locations[0]
    for i in matching_locations:
        park_zip_code = i["zipcode"]
        park_url = i["map"]
        park_activities = i["activities"]

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
MY_ZIP = park_zip_code
COUNTRY_CODE = os.getenv("COUNTRY_CODE", default="US")

def human_friendly_temp(my_temperature_f):
    """Rounds a decimal fahrenheit temperature to the nearest whole degree, adds degree symbol"""
    degree_sign = u"\N{DEGREE SIGN}"
    return f"{round(my_temperature_f)} {degree_sign}F"

def get_hourly_forecasts(zip_code=MY_ZIP, country_code=COUNTRY_CODE):
    # see: https://openweathermap.org/current
    request_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{country_code}&units=imperial&appid={OPEN_WEATHER_API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    #print(parsed_response.keys()) #> dict_keys(['cod', 'message', 'cnt', 'list', 'city'])
    result = {
        "city_name": parsed_response["city"]["name"],
        "hourly_forecasts": []
    }
    for forecast in parsed_response["list"][0:9]:
        #print(forecast.keys()) #> dict_keys(['dt', 'main', 'weather', 'clouds', 'wind', 'sys', 'dt_txt'])
        result["hourly_forecasts"].append({
            "timestamp": forecast["dt_txt"],
            "temp": human_friendly_temp(forecast["main"]["feels_like"]),
            "conditions": forecast["weather"][0]["description"]
        })
    return result

if __name__ == "__main__":

    if APP_ENV == "development":
        zip_code = MY_ZIP
        results = get_hourly_forecasts(zip_code=zip_code) # invoke with custom params
    else:
        results = get_hourly_forecasts() # invoke with default params

    print("-----------------")
    print(f"Weather Forecast for {park_id}...")
    print("-----------------")

    for hourly in results["hourly_forecasts"]:
        print(hourly["timestamp"], "|", hourly["temp"], "|", hourly["conditions"])

print("-----------------------------")

contact = input("For maps and park details, please enter your email: ")
user = input("Thanks! And your name: ")


SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
HIKER_EMAIL = contact

def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=HIKER_EMAIL, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None

MY_NAME = os.getenv("MY_NAME", default="Player 1")

if __name__ == "__main__":

    if APP_ENV == "development":
        zip_code = park_zip_code
        weather_results = get_hourly_forecasts(zip_code=zip_code) # invoke with custom params
    else:
        weather_results = get_hourly_forecasts() # invoke with default params

    #print(weather_results)

    html = ""
    html += f"<h3>Let's get going, {user}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"

    html += f"<h4>{park_id} is best known for...</h4>"
    html += f"<p>{park_activities}</p>"

    html += f"<h4>Download a map of {park_id} before your hike and save it offline:</h4>"
    html += f"<p>{park_url}</p>"

    html += f"<h4>Weather Forecast for {park_id}</h4>"
    html += "<ul>"
    for hourly in weather_results["hourly_forecasts"]:
        html += f"<li>{hourly['timestamp']} | {hourly['temp']} | {hourly['conditions'].upper()}</li>"
    html += "</ul>"

    html += f"<p>Now, go take a hike!</p>"

    send_email(subject="Your adventure awaits...", html=html)






# if __name__ == "__main__":

#     if APP_ENV == "development":
#         zip_code = park_zip_code
#         weather_results = get_hourly_forecasts(zip_code=zip_code) # invoke with custom params
#     else:
#         weather_results = get_hourly_forecasts() # invoke with default params

#     #print(weather_results)

#     html = ""
#     html += f"<h3>Greetings, {user}!</h3>"

#     html += "<h4>Today's Date</h4>"
#     html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"

#     html += f"<h4>Your park is known for: {park_activities.title()}</h4>"
#     html += f"<h4>Park Map: {park_url.title()}</h4>"
#     # html += f"<h4>Weather Forecast for {weather_results[{park_id}].title()}</h4>"
#     # html += "<ul>"
#     # for hourly in weather_results["hourly_forecasts"]:
#     #     html += f"<li>{hourly['timestamp']} | {hourly['temp']} | {hourly['conditions'].upper()}</li>"
#     # html += "</ul>"

#     send_email(subject="Your adventure awaits...", html=html)
