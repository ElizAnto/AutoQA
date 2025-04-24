"""Методы для проверки ответов запросов"""
import json


class Checking():

    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print(list(fields))
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'ОШИБКА, Значение обязательного поля не совпадает'
        # print(check_info)
        print(f"{field_name} верен!")

    """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info, 'ОШИБКА, Значение определенного слова в поле не совпадает'
        print(f"Слово {search_word} присутствует")