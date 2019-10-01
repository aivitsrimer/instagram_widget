import sqlite3


class SqliteDataStorage:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def get_clients(self):
        pass

    def get_client(self):
        pass

    def insert_client(self):
        pass

    def update_client(self):
        pass

    def get_photos(self, token):
        query = fr'''SELECT * FROM instagram_items INNER JOIN clients ON instagram_items.user_id = clients.user_id WHERE clients.access_token = "{token}" '''

        self._cursor.execute(query)
        result = self._cursor.fetchall()
        # return self.__extract_object(result)
        return result

    def insert_photo(self):
        pass

    def remove_photo(self):
        pass

    def get_objects(self):
        self._cursor.execute('SELECT * FROM objects')

        for row in self._cursor:
            yield self.__extract_object(row)

    def get_object(self, key: str) -> dict:
        self._cursor.execute('SELECT * FROM objects WHERE key = ?', key)
        return self.__extract_object(self._cursor.fetchone())

    @staticmethod
    def __extract_object(row):
        return {
            'original': row[0],
            'translation': row[1],
            'transcription': row[2],
        } if row else None
