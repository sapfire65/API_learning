import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

# Позитивный тест авторизации через API
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # запрос на авторизацию с логином и паролем
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        # Методы проверки валидности данных. Подготовка к дальнейшей работе.
        self.auth_sid = self.get_cokie(response1, "auth_sid") # проверка что поле "auth_sid" есть в ответе на запрос.
        self.token = self.get_header(response1, "x-csrf-token") # проверка что поле "x-csrf-token" есть в ответе на запрос.
        self.user_id_from_auth_metod = self.get_json_value(response1, "user_id") # Проверка формата ответа. Убеждаемся что он действительно JSON.


    # Проверяем что юзер действительно авторизовался.
    def test_auth_user(self):
        response2 = requests.get(
           'https://playground.learnqa.ru/api/user/auth',
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_metod,
            "значение user_id из авторизации не равен user_id из валидации"
        )


    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token': self.token}
            )

            print(condition)
        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid': self.auth_sid}
            )
            print(condition)

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"Пользователь авторизован не смотря на значение  - '{condition}'"
        )







