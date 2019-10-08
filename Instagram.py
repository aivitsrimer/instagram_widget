from urllib import parse
from HttpClient import *
import json
from ApplicationSettings import application_settings


class Instagram:

    def __init__(self, token=None):
        self._access_token = token
        self._http_client = HttpClient()
        self.error_msg = False

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
        try:
            self._check_exists_token()
            url = self._build_api_url(path)
            response = self._http_client.send_request(url)
            parsed_response = json.loads(response)

            return parsed_response['data']
        except Exception as e:
            self.error_msg = e
            print(e)
            return False

    def _build_api_url(self, path, params=None):
        """
        Собирает URL для запроса
        :param path: end point Инстаграма
        :param params: параметры для запроса
        :return: URL
        """
        try:
            url = 'https://api.instagram.com/v1/'
            params = {'access_token': self._access_token}
            return url + path + '/?' + parse.urlencode(params)
        except Exception as e:
            self.error_msg = e
            print(e)
            return False

    def _check_exists_token(self):
        if not self._access_token:
            raise Exception('Token is None')


def test_access_token(api):
    try:
        print(api.access_token)
        api.access_token = 'b123'
        print(api.access_token)
    except Exception as e:
        print(e)
    return 'All good'


if __name__ == '__main__':
    api = Instagram(application_settings.token)
    print(test_access_token(api))
