"""
Данная программа получает фотографии из аккаунта Инстаграм через API.
    Для работы используется access_token, указанный в конфиге и заранее сохраненный в базе данных.
    Сохраняет фотографии в базу данных, которые можно получить в виде html или json.
    Количество выводимых виджетом фотографий задается в конфиге.
    Также можно получить json ответ от Инстаграма или виджета.
    Если введен некорректный access_token или его срок действия истек, выведется ошибка.

Ссылки:
    / - главная страница с навигацией по остальным.
    /widget - html страница виджета, где выводятся фотографии.
    /api/media - json ответ от API Инстаграма.
    /api/widget - json ответ от виджета, чтобы кастомизировать виджет по-своему.


Возможные улучшения интепфейса:
    1. Добавить ник клиента в базу для отображения ника в виджете и ссылку на аккаунт для перехода.
    2. Красивое оформление виджета, необходимо изучение html, css и js.
Поддержка нескольких пользователей:
    1. Добавить сохранение access_token и user_id в таблицу clients в бд.
    2. Необходимо дополнительно на js написать сохранение access_token
        из-за особенностей получения access_token от Инстаграма.
    3. Система регистрации разных пользователей по логину и паролю.

"""


from Instagram import Instagram
from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage
from UpdateDataStorage import update_db
import WebController


def start():
    access_token = application_settings.token
    api = Instagram(access_token)
    db = SqliteDataStorage(application_settings.db_name)

    update_db(api, db)

    WebController.start_server(
        application_settings.web_host,
        application_settings.web_port,
        application_settings.templates_path,
        api, db)


if __name__ == '__main__':
    start()
