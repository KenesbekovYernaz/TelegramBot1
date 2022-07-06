import requests
import datetime
import config

class Parser_Weather:

	def get_weather(self, city_name):
		weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config.WEATHER_KEY}&units=metric").json()
		info = f"""<b>***{datetime.datetime.today()}***</b>
		<b>Гороп:</b> <code>{weather_info["name"]}</code>
		<b>Страна:</b> <code>{weather_info["sys"]["country"]}</code>
		<b>Температура:</b> <code>{weather_info["main"]["temp"]}°C</code>
		<b>Облака:</b> <code>{weather_info["clouds"]["all"]}</code>
		<b>Влажность:</b> <code>{weather_info["main"]["humidity"]}</code>
		<b>Давлене:</b> <code>{weather_info["main"]["pressure"]}</code>
		<b>Направление Ветра:</b> <code>{weather_info["wind"]["deg"]}°</code>
		<b>Скорость Ветра:</b> <code>{weather_info["wind"]["speed"]} m/s</code>"""

		return info
		# City: Город
		# Country: Страна
		# Temp: Температура
		# Clouds: Облака
		# Humidity: Влажность
		# Pressure: Давление
		# Wind Direction: Направление Ветра
		# Wind Speed: Скорость Ветра
