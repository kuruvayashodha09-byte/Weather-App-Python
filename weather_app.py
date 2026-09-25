print("===== WEATHER APP =====")

city = input("Enter city name: ")

weather = {
    "Hyderabad": {
        "temperature": "30°C",
        "condition": "Sunny"
    },
    "Delhi": {
        "temperature": "28°C",
        "condition": "Clear"
    },
    "Mumbai": {
        "temperature": "29°C",
        "condition": "Cloudy"
    },
    "Chennai": {
        "temperature": "31°C",
        "condition": "Sunny"
    },
    "Bangalore": {
        "temperature": "25°C",
        "condition": "Rainy"
    }
}

if city in weather:
    print("\nCity:", city)
    print("Temperature:", weather[city]["temperature"])
    print("Condition:", weather[city]["condition"])
else:
    print("\nWeather information not available for this city.")

print("\nThank you for using the Weather App!")
