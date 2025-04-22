SeleniumProject1: test buy product on site https://www.saucedemo.com/ 

... description ...

SeleniumProject2: test buy product on site https://www.onlinetrade.ru

Запуск теста с аннотацией шагов в терминале: python -m pytest -s -v

Запуск теста python pytest

Важно! Пройти тест до финиша, поскольку в процессе добавляется товар в корзину и в конце удаляется из корзины для успешного повторного теста.

Тест test_buy_product: 
1. login: Авторизация
2. smart: Страница со смартфонами
3. filters: Выбор фильтров
4. product: Выбор отфильтрованного смартфона
5. cart: Переход в корзину
6. client_information: Добавление информации о клиенте (без нажатия на кнопку для финального заказа)
7. clear_cart: Очистка корзины

Дополнения:
+ conftest
+ logger
+ allure