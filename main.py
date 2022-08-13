import requests

pyload = {"name": "User"}

responce = requests.get("https://playground.learnqa.ru/api/hello", params=pyload)
print(responce.text)


