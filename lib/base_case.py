import json

from requests import Response

class BaseCase:
    # проверка наличия куки, и если они есть, записать куки в значение переменной.
    def get_cokie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"куки - {cookie_name}, не найден в ответе"
        return response.cookies[cookie_name]


    def get_header(self, reasponse: Response, headers_name):
        assert  headers_name in reasponse.headers, f"Заголовок - {headers_name}, не найден в ответе"
        return reasponse.headers[headers_name]

    # функция проверки формата ответа. Убеждаемся что он действительно JSON.
    def get_json_value(self, responce: Response, name):
        try:
            responce_as_dict = responce.json()
        except json.decoder.JSONDecodeError:
            assert False , f"Ответ не в формате JSON. Текст ответа '{responce.text}'"

        assert  name in responce_as_dict, f"В ответе JSON нет значения '{name}' "
        # Если проверка не упала, возвращаем в функцию, значение name
        return responce_as_dict[name]

