import paho.mqtt.client as mqtt # type: ignore
import requests # type: ignore
import time

# WeatherAPI key 
WEATHER_API_KEY = "820be25f15e54b92aec185808252901"

# City for weather data
CITY = "New York"  

# MQTT Broker & Topic
broker = "mqtt.eclipseprojects.io"
topic = "sensor/weather"

# Function to fetch real-time weather data
def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}&aqi=yes"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for failed requests
        
        data = response.json()
        condition = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        aqi = data["current"]["air_quality"]["pm2_5"]  # Fine particulate matter

        weather_info = (f"Weather: {condition}, Temperature: {temperature}°C, "
                        f"Humidity: {humidity}%, Wind Speed: {wind_speed} km/h, AQI: {aqi}")
        return weather_info

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"

# Connect to MQTT Broker
client = mqtt.Client()
client.connect(broker, 1883)

# Publish weather data at intervals
while True:
    weather_info = get_weather()
    client.publish(topic, weather_info)
    print(f"Published: {weather_info}")
    
    time.sleep(10)  # Fetch and publish weather data every 10 minutes