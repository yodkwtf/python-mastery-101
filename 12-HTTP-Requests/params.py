import requests

url = "http://icanhazdadjoke.com/search"

response = requests.get(
  url, 
  headers={"Accept": "application/json"},
  params={
    "term": "cat",
    "limit": 2
  }
) 

data = response.json() 

print(data['results'])
# print(data['results'][1]['joke'])
