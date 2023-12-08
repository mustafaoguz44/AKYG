import requests
url="https://meowfacts.herokuapp.com/?count=3"
response=requests.get(url)
data=response.json()
print(data)
