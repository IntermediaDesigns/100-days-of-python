import requests
import json
from datetime import date

timezone = "America/New_York"
latitude = 39.202057
longitude = -76.750157

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone}")

weather_data = result.json()


today = date.today().strftime("%Y-%m-%d")
today_index = weather_data['daily']['time'].index(today)
weather_code = weather_data['daily']['weathercode'][today_index]
max_temp = weather_data['daily']['temperature_2m_max'][today_index]
min_temp = weather_data['daily']['temperature_2m_min'][today_index]


if weather_code == 0:
    weather_description = "☀️ Clear sky"
elif weather_code == 1 or weather_code == 2 or weather_code == 3:
    weather_description = "🌥️ Partly cloudy"
elif weather_code == 45 or weather_code == 48:
    weather_description = "🌫️ Foggy"
elif weather_code in [51, 53, 55, 56, 57]:
    weather_description = "💧 Drizzle"
elif weather_code in [61, 63, 65, 66, 67]:
    weather_description = "☔ Rain"
elif weather_code in [71, 73, 75, 77]:
    weather_description = "❄️ Snow"
elif weather_code in [80, 81, 82]:
    weather_description = "☔ Rain showers"
elif weather_code in [85, 86]:
    weather_description = "🌨️ Snow showers"
elif weather_code in [95, 96, 99]:
    weather_description = "🌩️ Thunderstorm"
else:
    weather_description = "Unknown"


print("\n╔══════════════════════════════════════╗")
print("║      Today's Weather in Maryland     ║")
print("╠══════════════════════════════════════╣")
print(f"║ Date: {today:<30} ║")
print(f"║ Weather: {weather_description: <26}   ║")
print(f"║ Max Temperature: {max_temp:>5.1f}°C             ║")
print(f"║ Min Temperature: {min_temp:>5.1f}°C             ║")
print("╚══════════════════════════════════════╝")