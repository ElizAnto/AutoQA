from utils.api import GoogleMapsAPI

"""Создание, изменение и удаление новой локации"""

class TestCreatePlace():

    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # Вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки создания новой локации

        print("Метод PUT")
        result_put = GoogleMapsAPI.put_new_place(place_id)  # Вызов метода для изменения новой локации

        print("Метод GET PUT")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки изменения новой локации

        print("Метод DELETE")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)  # Вызов метода для удаления новой локации

        print("Метод GET DELETE")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки удаления новой локации