# -*- coding: utf-8 -*-

from urllib import parse, request


class HttpClient(object):

    @staticmethod
    def send_request(url, params=None, timeout=30):
        post_data = parse.urlencode(params) if params else None

        response = request.urlopen(
            url, post_data.encode() if post_data else None, timeout
        )

        return response.read()
