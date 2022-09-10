import requests

# responce = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#
# first_responce = responce.history[0] # Обращаемся к истории запросов и выбираем первый запрос
# second_responce = responce # Итоговый запрос
#
# print(first_responce.url) # Вывести URL запроса
# print(second_responce.url) # Вывести URL запроса
#
#
# print()
# print(responce.status_code) # Получаем статус код страницы (будет сравниватся с ожидаемым кодом)
# print(responce.text) # Выводим и код ответа и текст страницы

'''
Домашнее задание:

С помощью конструкции response.history необходимо узнать, 
сколько редиректов происходит от изначальной точки назначения до итоговой. 
И какой URL итоговый.'''

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
all_redirect = len(response.history)
print(f'Количество редиректов: {all_redirect - 1}')
print(f'Итоговый URL: {response.url}')
