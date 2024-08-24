# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
from urllib3 import request

import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
#из базового адреса сервиса и пути к его документации, оба определены в модуле
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
#на результат выполнения запроса.

#ЗАДАНИЕ_1
# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Вызываем функцию get_docs и сохраняем результат в переменную response
#response = get_docs()

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
#print(response.json())

#ЗАДАНИЕ_2_3_4
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":200})
#response = get_logs()
#print(response.status_code)
#print(response.headers)

#ЗАДАНИЕ_5_6
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
#response = get_users_table()
#print(response.status_code)

#ТЕМА POST-запрос

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
#response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
#print(response.status_code)
#print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)
response = post_products_kits(data.products_ids)
print(response.status_code)
print(response.json())
