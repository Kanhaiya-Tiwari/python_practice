import requests

API_KEY = "2921ba050b39b48d6082a762be453766"
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
    
    data = response.json()
    
    # Validate response structure
    if "main" not in data or "weather" not in data:
        print("Error: Invalid API response structure")
    else:
        temperature = data["main"].get("temp", "N/A")
        humidity = data["main"].get("humidity", "N/A")
        weather = data["weather"][0].get("description", "N/A") if data["weather"] else "N/A"
        
        print(f"Temp: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except ValueError:
    print("Error: Invalid JSON response from API")
except Exception as e:
    print(f"Unexpected error: {e}")