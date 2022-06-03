import requests
from termcolor import colored
from pyfiglet import figlet_format
from random import choice

title = colored(figlet_format("Dad Joke OP"), color="cyan")
url = "http://icanhazdadjoke.com/search"

# start the app

def getJokeResult(results):
  if len(results) == 0:
    return f"Sorry, I don't have any jokes about {topic}! Please try again."
  elif len(results) == 1:
    return f"I've got one joke about {topic}. Here it is: \n {results[0]['joke']}"
  else:
    return f"I've got {len(results)} jokes about {topic}. Here's one: \n {choice(results)['joke']}"

# print title
print(title)

# get user's topic
topic = input ("Let me tell you a joke! Give me a topic: ")

# get all jokes
response = requests.get(
  url, 
  headers={"Accept": "application/json"},
  params={
    "term": f"{topic}",
  }
) 
data = response.json()

# get result
result = getJokeResult(data['results'])
print(result)