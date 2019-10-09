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
import WebController


def start():
    access_token = application_settings.token
    api = Instagram(access_token)
    media = api.media()

    if not media:
        print(api.error_msg)
    else:
        media_data = InstagramItem.retrieve_list(media)
        return media_data

    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(access_token, application_settings.widget_photo_limit)
    db_data = InstagramItem.retrieve_list(data)

    InstagramItem.compare_and_save_to_db(media_data, db_data, db)

    WebController.start_server(
        application_settings.web_host,
        application_settings.web_port,
        application_settings.templates_path)


if __name__ == '__main__':
    start()
