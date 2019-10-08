"""


Для поддержки нескольких пользователей нужно дополнительно на js
    написать сохранение access token
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
    media_data = InstagramItem.retrieve_list(media)

    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(access_token)
    db_data = InstagramItem.retrieve_list(data)

    InstagramItem.compare_and_save_to_db(media_data, db_data, db)

    WebController.start_server(
        application_settings.web_host,
        application_settings.web_port,
        application_settings.templates_path)


if __name__ == '__main__':
    start()
