from Instagram import Instagram
from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage
from InstagramItem import InstagramItem

access_token = application_settings.token
api = Instagram(access_token)
# print(api.media())
db = SqliteDataStorage(application_settings.db_name)
data = db.get_photos(application_settings.token)
print(InstagramItem.retrieve_list(data))
