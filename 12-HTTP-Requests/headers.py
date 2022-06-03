from urllib import response
import requests

url = "http://icanhazdadjoke.com/"

# response = requests.get(url) 
# print(response.text) # returns html

# response = requests.get(url, headers={"Accept": "text/html"}) 
# print(response.text) # same as above

# response = requests.get(url, headers={"Accept": "text/plain"}) 
# print(response.text) # returns the main data

response = requests.get(url, headers={"Accept": "application/json"}) # returns json
data = response.json() # converts json into python code
print(data['joke'])
