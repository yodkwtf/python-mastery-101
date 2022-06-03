import requests

url = "http://google.com/yodkwtf"

response = requests.get(url)

print(f"You response to {url} came back with a status code {response.status_code}")