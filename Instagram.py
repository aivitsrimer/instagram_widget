from urllib import parse
from HttpClient import *
import json


class Instagram:

    def __init__(self):
        self._access_token = '20261245390.1677ed0.f9d9fd4ebb134fde90dc9ef54d443fa8'
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


def test_access_token(api):
    try:
        print(api.access_token)
        api.access_token = 'b123'
        print(api.access_token)
    except Exception:
        return 'Fail'
    return 'All good'


if __name__ == '__main__':
    api = Instagram()
    api.access_token = '2258522848.1677ed0.e289f430fd484cceb42ae8d0f0ad85b6'
    # print(test_access_token(api))
    print(api.media())
