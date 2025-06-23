import requests

api_key ="5a64f50deed06cee4a5ebe018c0a1b13"
city=input("Enter city name: ")


url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

try:
    
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    
    
    temperature = data['main']['temp'] - 273.15
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description.capitalize()}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except keyError:
    print("Invalid city name")