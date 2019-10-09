"""


Возможные улучшения:
Добавить имя клиента в базу для отображения ника в виджете и ссылку на аккаунт для перехода.
Красивое оформление виджета, необходимо изучение html, css и js.
Поддержка нескольких пользователей, необходимо дополнительно на js написать сохранение access token
    из-за особенностей получения access token от Инстаграма.
"""


from Instagram import Instagram
from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage
from InstagramItem import InstagramItem
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
