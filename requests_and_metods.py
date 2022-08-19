import requests
import json
from  colorama  import  Fore ,  Back ,  Style

'''
ДОМАШЕЕ ЗАДАНИЕ:

С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. 
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. 
И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, 
но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=
'''

a = '{"method":[{"method":"DELETE"}, {"method":"PUT"}, {"method":"GET"}, {"method":"POST"}, {"method":"HEAD"}]}'
obj = json.loads(a)

# my_request = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type") # без параметра method
# print(f"Запрос без параметра 'method': {my_request.text}")
#
# my_request_1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj["method"][4])
# print(f"Запрос c параметром 'HEAD': {my_request_1.text}")
#
# my_request_1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj["method"][3])
#
# print(f"Запрос c правильным параметром 'POST': {my_request_1.text}")
# print()

# перебор всех возможных параметров циклом
for m in range(0, 4):
    request_method = str(obj["method"][m]["method"])
    print()
    print(Fore.YELLOW, request_method, Style.RESET_ALL, sep='__', end='\n')

    for i in range(0, 5):
        param_value = obj["method"][i]
        if request_method == "GET":
            pass_value = {"params": param_value}
        else:
            pass_value = {"data": param_value}

        req = requests.request(request_method, "https://playground.learnqa.ru/ajax/api/compare_query_type", **pass_value)


        if request_method not in str(param_value) and req.text == '{"success":"!"}':
            print(Fore.BLUE, f'Метод запроса', Fore.RED, request_method, Style.RESET_ALL, f' Значение метода:', Fore.RED, obj["method"][i]["method"], Style.RESET_ALL, f'*', Style.RESET_ALL, end='')
            print(Fore.GREEN, f'logined /', Style.RESET_ALL, end='')
            print(Fore.RED, f'BUG !!! -  ОТВЕТ: {req.text}', Style.RESET_ALL)

        elif request_method in str(param_value) and req.text == '{"success":"!"}':
            print(Fore.BLUE, f'Метод запроса', Fore.GREEN, request_method, Style.RESET_ALL, f' Значение метода:', Fore.GREEN, obj["method"][i]["method"], Style.RESET_ALL, f'*', Style.RESET_ALL, end='')
            print(Fore.GREEN, f'logined /', Style.RESET_ALL, end='')
            print(Fore.GREEN, f'OK - ОТВЕТ: {req.text}', Style.RESET_ALL)

        print(Fore.BLUE, f'Метод запроса  {request_method} | Значение метода: {obj["method"][i]["method"]} -',Fore.BLUE, f'ОТВЕТ: {req.text}', Style.RESET_ALL)


