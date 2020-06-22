 
import requests, json 
 
api_key = "ff0e163351ced87f0f50b75a53c45020"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 


complete_url = base_url + "appid=" + api_key + "&q=" + city_name 


response = requests.get(complete_url) 


x = response.json() 

if x["cod"] != "404": 

	y = x['main'] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 
