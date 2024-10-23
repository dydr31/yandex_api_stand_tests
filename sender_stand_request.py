# Импортируем необходимые библиотеки и модули
import requests
import configuration
import data


# Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
# def get_logs():
#     # Складываем базовый URL из конфигурационного файла и путь к основным логам,
#     # чтобы сформировать полный URL для запроса.
#     # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
#     return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})
#
#
# # Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
# response = get_logs()
#
# # Выводим в консоль HTTP-статус код ответа сервера. Коды состояния HTTP сообщают
# # о результате выполнения запроса. Например, код 200 означает "OK", а 404 - "Не найдено".
# print(response.status_code)

# Выводим в консоль заголовки HTTP-ответа сервера.
# Заголовки могут содержать полезную информацию, например, тип содержимого ответа
# и используемые сервером технологии.
# print(response.headers)

# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Вывод статус-кода ответа сервера в консоль
# Статус-коды HTTP сообщают о результате выполнения запроса
print(response.status_code)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


# def post_products_kits(products_ids):
#     # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
#     # Возвращается объект ответа, полученный от сервера
#     return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
#                          json=products_ids,
#                          headers=data.headers)
#
# response = post_products_kits(data.product_ids)
#
# print(response.status_code)
# print(response.json())