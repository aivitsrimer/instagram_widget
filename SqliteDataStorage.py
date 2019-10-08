import sqlite3


class SqliteDataStorage:
    def __init__(self, db_path):
        self._connection = None
        try:
            self._connection = sqlite3.connect(db_path)
        except Exception as e:
            print(e)

        self._cursor = self._connection.cursor()

    def get_photos(self, token, widget_photo_limit):
        query = fr'''SELECT instagram_items.photo_id, instagram_items.photo_link, instagram_items.user_id, 
        instagram_items.created_time FROM instagram_items INNER JOIN clients ON 
        instagram_items.user_id = clients.user_id WHERE clients.access_token = "{token}" 
        ORDER BY instagram_items.created_time DESC LIMIT {widget_photo_limit}'''

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result

    def insert_photo(self, photo_id, photo_link, user_id, created_time):
        try:
            query = fr'''INSERT INTO instagram_items(photo_id, photo_link, user_id, created_time) 
            VALUES("{photo_id}", "{photo_link}", "{user_id}", "{created_time}")'''
            self._cursor.execute(query)
        except sqlite3.IntegrityError as e:
            print(e)
        self._connection.commit()
        return self._cursor.lastrowid

    def remove_photo(self):
        pass
