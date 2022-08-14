import requests

responce = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

first_responce = responce.history[0] # Обращаемся к истории запросов и выбираем первый запрос
second_responce = responce # Итоговый запрос

print(first_responce.url) # Вывести URL запроса
print(second_responce.url) # Вывести URL запроса



# print(responce.status_code) # Получаем статус код страницы (будет сравниватся с ожидаемым кодом)
# print(responce.text) # Выводим и код ответа и текст страницы

