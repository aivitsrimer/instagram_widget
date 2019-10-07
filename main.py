"""


Для поддержки нескольких пользователей нужно дополнительно на js
    написать сохранение access token
"""


from Instagram import Instagram
from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage
import WebController


def start():
    access_token = application_settings.token
    api = Instagram(access_token)
    # print(api.media())
    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(application_settings.token)
    # print(InstagramItem.retrieve_list(data))
    WebController.start_server(
        application_settings.web_host,
        application_settings.web_port,
        application_settings.templates_path)


if __name__ == '__main__':
    start()
