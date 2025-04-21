SeleniumProject1: test buy product on site https://www.saucedemo.com/ 

... description ...

SeleniumProject2: test buy product on site https://www.onlinetrade.ru

Запуск теста в терминале PyCharm: python -m pytest -s -v

Важно! Пройти тест до финиша, поскольку в процессе добавляется товар в корзину и в конце удаляется из корзины для успешного повторного теста.

Тест test_buy_product: 
-  login: Авторизация
-  smart: Страница со смартфонами
-  filters: Выбор фильтров
-  product: Выбор отфильтрованного смартфона
-  cart: Переход в корзину
-  client_information: Добавление информации о клиенте (без нажатия на кнопку для финального заказа)
-  clear_cart: Очистка корзины
