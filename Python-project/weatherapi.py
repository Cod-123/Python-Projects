#requests tend to serve an endpoint for the data you want to get.in order to make a request to the API, you need to know the URL of the endpoint you want to use. 
import requests

API_KEY='2fd12545a95e925217919cfe171a10a6'

# the base url is the url of the endpoint you want to use.
BASE_URL='http://api.openweathermap.org/data/2.5/weather'

city_name=input('Enter the name of the city: ')

# the request url is the base url with the parameters you want to pass to the endpoint.f string embeds the values of the variables in the string.
# where the appid is the API key and q is the city name which are query parameters.
request_url=f"{BASE_URL}?appid={API_KEY}&q={city_name}"

#a get request is made using the request url. and the response given contains the data related to the city
response=requests.get(request_url)

# the status code of the response is checked to see if the request was successful. and if so data is returned in json format.
if response.status_code==200:
    data = response.json()

    #weather is returned as a list of dictionaries. so the dictionary with key weather is selected which is returned as a list and the description attribute is accessed frm it
    weather=data['weather'][0]['description']
    print("The weather is:",weather)

    temperature=data['main']['temp']
    print("The temperature in kelvin is: ",temperature)


    print(data)
else:
    print('Error in the request')
   


