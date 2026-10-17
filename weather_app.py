import requests


def get_weather():
    print("\n===== WEATHER APPLICATION =====")

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    # Enter your OpenWeather API key here
    api_key = "YOUR_API_KEY"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        if response.status_code == 401:
            print("Invalid API key or API key not yet active.")
            return

        if response.status_code == 404:
            print("City not found. Please check the spelling.")
            return

        response.raise_for_status()

        data = response.json()

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display results
        print("\n------ WEATHER REPORT ------")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temperature} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.title()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("----------------------------")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("Unable to fetch weather data:", error)

    except (KeyError, IndexError, TypeError, ValueError):
        print("Unable to process the weather information.")


if __name__ == "__main__":
    get_weather()