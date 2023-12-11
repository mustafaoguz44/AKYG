import requests
url="https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/tur-abdulbakigolpin-la.json"
response=requests.get(url)
data=response.json()
print(data)
