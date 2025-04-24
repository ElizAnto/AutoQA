import requests
from utils.logger import Logger

"""Список HTTP методов"""

class HttpMethod:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod # Позволяет вызывать функцию откуда угодно
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
        Logger.add_response(result)
        return result