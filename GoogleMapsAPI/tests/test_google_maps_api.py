from utils.api import GoogleMapsAPI
from utils.checking import Checking
import allure

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class TestCreatePlace():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # Вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки создания новой локации
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = GoogleMapsAPI.put_new_place(place_id)  # Вызов метода для изменения новой локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки изменения новой локации
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)  # Вызов метода для удаления новой локации
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки удаления новой локации
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])
        # # Без проверки наличия определенного слова в ответе
        # Checking.check_json_value(result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Тестирование создания, изменения и удаления новой локации завершено успешно")