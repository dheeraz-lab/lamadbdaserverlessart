import requests
import os

def lambda_handler(event, context):
    city = "New York"
    api_key = os.environ.get('WEATHER_API_KEY')  # Set in Lambda environment variables
    if not api_key:
        return {"statusCode": 500, "body": "API key not configured."}
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data['main']['temp']
        print(f"Current temperature in {city} is {temperature}°C")
        return {
            "statusCode": 200,
            "body": f"Current temperature in {city} is {temperature}°C"
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {
            "statusCode": 500,
            "body": "Failed to fetch weather data"
        }
