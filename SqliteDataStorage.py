import sqlite3

# TODO добавить имя клиента в базу, ссылку на аккаунт для перехода


class SqliteDataStorage:
    def __init__(self, db_path):
        self._connection = None
        try:
            self._connection = sqlite3.connect(db_path)
        except Exception as e:
            print(e)

        self._cursor = self._connection.cursor()

    def get_photos(self, token):
        query = fr'''SELECT instagram_items.photo_id, instagram_items.photo_link, instagram_items.user_id FROM 
        instagram_items INNER JOIN clients ON instagram_items.user_id = clients.user_id WHERE 
        clients.access_token = "{token}" '''

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def insert_photo(self, photo_id, photo_link, user_id):
        try:
            query = fr'''INSERT INTO instagram_items(photo_id,photo_link,user_id) VALUES("{photo_id}","{photo_link}","{user_id}")'''
            self._cursor.execute(query)
        except sqlite3.IntegrityError as e:
            print(e)
        self._connection.commit()
        return self._cursor.lastrowid


    def remove_photo(self):
        pass
