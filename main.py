import requests
import schedule
import time
import twilio.rest 

def get_weather_data(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,apparent_temperature,precipitation,rain"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_message(message):
    print(message)
    account_sid = ""
    auth_token = ""
    from_number = ""
    to_number = "+40766463787"
    
    client = twilio.rest.Client(account_sid, auth_token)
    message = client.messages.create(
        body=message, from_=from_number, to=to_number
    )
    
    print("Message sent")
    

def send_weather_update():
    print("Sending weather update")
    # Latitude and longitude for the location you want to get the weather for
    lat = 45.037556
    lon = 23.270751
    weather_data = get_weather_data(lat, lon)
    temperature = weather_data["hourly"]["temperature_2m"][0]
    apparent_temperature = weather_data["hourly"]["apparent_temperature"][0]
    precipitation = weather_data["hourly"]["precipitation"][0]
    rain = weather_data["hourly"]["rain"][0]
    
    weather_info = (
        f"Good morning Jefe!\n\n"
        f"Temperature: {temperature}\n"
        f"Apparent temperature: {apparent_temperature}\n"
        f"Precipitation: {precipitation}\n"
        f"Rain: {rain}\n"
    )
    send_message(weather_info)
    

def main():
    schedule.every().day.at("12:53").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()