from InstagramItem import InstagramItem
from ApplicationSettings import application_settings


def update_db(api, db):
    data = db.get_photos(application_settings.token, application_settings.widget_photo_limit)
    media = api.media()
    if not media:
        print(api.error_msg)
        return

    media_data = InstagramItem.retrieve_list(media)
    db_data = InstagramItem.retrieve_list(data)

    InstagramItem.compare_and_save_to_db(media_data, db_data, db)
