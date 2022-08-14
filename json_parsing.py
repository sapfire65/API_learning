import json

# string_as_json_format = '{"answer": "Hello, word"}'
# obj = json.loads(string_as_json_format)
# key = "answer"
#
# if key in obj:
#     print(obj[key])
# else:
#     print(f'Ключа {key} в JSON нет!')


"""
Домашнее задание.
Наша задача с помощью библиотеки “json”, распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.
"""
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj = json.loads(json_text)
print(obj["messages"][1])

