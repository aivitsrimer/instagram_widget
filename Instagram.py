from urllib import parse
from HttpClient import *
import json
import ApplicationSettings
from SqliteDataStorage import SqliteDataStorage

class Instagram:

    def __init__(self, token=None):
        self._access_token = token
        self._http_client = HttpClient()

    def media(self):
        response = self._get('users/self/media/recent')
        return response

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    def _get(self, path):
        """
        Получает ответ от API
        :return: словарь из json ответа
        """
        self._check_exists_token()
        url = self._build_api_url(path)
        response = self._http_client.send_request(url)
        parsed_response = json.loads(response)
        # print(url)

        # TODO обработать ошибки

        return parsed_response['data']

    def _build_api_url(self, path, params=None):
        """
        Собирает URL для запроса
        :param path: end point Инстаграма
        :param params: параметры для запроса
        :return: URL
        """
        url = 'https://api.instagram.com/v1/'
        params = {'access_token': self._access_token}
        return url + path + '/?' + parse.urlencode(params)

    def _check_exists_token(self):
        if not self._access_token:
            raise Exception('Token is None')


def test_access_token(api):
    try:
        print(api.access_token)
        api.access_token = 'b123'
        print(api.access_token)
    except Exception:
        return 'Fail'
    return 'All good'


if __name__ == '__main__':
    access_token = ApplicationSettings.application_settings.token
    api = Instagram(access_token)
    # print(test_access_token(api))
    # print(api.media())
    db = SqliteDataStorage(ApplicationSettings.application_settings.db_name)
    print(db.get_photos(ApplicationSettings.application_settings.token))
