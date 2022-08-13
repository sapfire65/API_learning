from  json.decoder import JSONDecodeError
import requests

responce = requests.get("https://playground.learnqa.ru/api/get_text")
print(responce.text)

try:
    parsed_respnse_text = responce.json()
    print(parsed_respnse_text)

except JSONDecodeError:
    print('Response is not a JSON format')





# pyload = {"name": "User"}
# responce = requests.get("https://playground.learnqa.ru/api/hello", params=pyload)
# print(responce.text)