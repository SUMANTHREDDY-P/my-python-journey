from datetime import datetime
import requests

Key = "API_KEY"  # Replace with your actual OpenWeatherMap API key
city_name = input("Enter the city name: ")
def  get_wether_data(city_name):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
    data = r.json()
    if data["cod"] == 200:
        temp =round(data["main"]["temp"] - 273.15,1) 
        humidity = data["main"]["humidity"]
        country = data["sys"]["country"]
        unix_timestamp = data["dt"]

        
        def timestamp_to_datetime(unix_timestamp):
        
            dt = datetime.fromtimestamp(unix_timestamp)
            return dt.strftime("%Y-%m-%d %I:%M:%S %p %z")
        
        return f"Temperature: {temp}, Humidity: {humidity}, 'City: {city_name}/Country: {country}', Date and Time: {timestamp_to_datetime(unix_timestamp)}"
    else:
        print("City not found or error occurred.")
        return None





print(get_wether_data(city_name))
