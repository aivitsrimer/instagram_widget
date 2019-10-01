from Instagram import Instagram
from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage

access_token = application_settings.token
api = Instagram(access_token)
# print(api.media())
db = SqliteDataStorage(application_settings.db_name)
print(db.get_photos(application_settings.token))
