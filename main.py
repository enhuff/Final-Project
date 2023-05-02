#Importing weather information
import json, requests
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "8959cd04dcedced9b2aff769b3ff4bb7"
#requesting the city from the user and testing to make sure it is a valid city
while True:
  choice = int(input("Please type 1 to enter a city for the weather,or 2 to quit:"))
  print("")
  if choice == 1:
#Using a try except block to check if the city name is legitamte
    try:
      city = (input("Please input a city that you would like todays temperature for: "))
      print("")
#pulling up the website
      url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
      response = requests.get(url)
      unformated_data = response.json()
      temp = unformated_data["main"]["temp"]
      maxtemp = unformated_data["main"]["temp_max"]
      url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
      response = requests.get(url)
      unformated_data = response.json()
      temp = unformated_data["main"]["temp"]
#printing out the information for the user
      print(f"The current temperature is: {temp}\N{DEGREE SIGN}")
      maxtemp = unformated_data["main"]["temp_max"]
      print(f"The high temperature for today is: {maxtemp}\N{DEGREE SIGN}")
      print("")
#rejecting the incorrect city name
    except KeyError:
      print("Invlaid City, please input a valid city name")
      print("")
#how to close the program when they are done   
  elif choice == 2:
    print("Thank you for using my program.")
    break