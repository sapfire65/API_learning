import requests

payload = {"login":"secret_login", "password":"secret_pass"}

# авторизация по логину и паролю в словаре "payload"
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get('auth_cookie')  # получаем куки. Называем ключь как - "auth_cookie"

cookies = {}

# Если "cookie_value" не пустой
if cookie_value is not None:
    # добавляем в массив куки
    cookies.update({'auth_cookie': cookie_value})
    print(dict(cookies))
else:
    print(dict(cookies))

"""
Проверяем авторизован ли пользователь или нет.
Передаем либо готовые куки либо ничего. 
Ответ получаем из текста на странице
"""
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)
