import sqlite3

# TODO добавить имя клиента в базу, ссылку на аккаунт для перехода


class SqliteDataStorage:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def get_photos(self, token):
        query = fr'''SELECT instagram_items.photo_id, instagram_items.photo_link FROM instagram_items INNER JOIN +
         clients ON instagram_items.user_id = clients.user_id WHERE clients.access_token = "{token}" '''

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def insert_photo(self):
        pass

    def remove_photo(self):
        pass
