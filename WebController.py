from pathlib import Path

import jinja2
from aiohttp import web
import aiohttp_jinja2

from InstagramItem import InstagramItem
from Instagram import Instagram

from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage

from UpdateDataStorage import update_db


routes = web.RouteTableDef()

__api: Instagram = None
__db: SqliteDataStorage = None


@routes.get('/')
@aiohttp_jinja2.template('main_page.jinja2')
async def main_page(request: web.Request):
    pass


@routes.get('/widget')
@aiohttp_jinja2.template('widget.jinja2')
async def widget(request: web.Request):
    name = 'Photos'
    update_db(__api, __db)
    if __api.error_msg:
        return {'name': name, 'photos': None, 'error': __api.error_msg}

    data = __db.get_photos(application_settings.token, application_settings.widget_photo_limit)
    photos = InstagramItem.retrieve_list(data)

    return {'name': name, 'photos': photos, 'error': __api.error_msg}


@routes.get('/api/media')
async def api_media(request: web.Request) -> web.Response:
    if __api.error_msg:
        return web.json_response(_json_error(__api.error_msg))
    return web.json_response(__api.media())


@routes.get('/api/widget')
async def api_widget(request: web.Request) -> web.Response:
    update_db(__api, __db)
    if __api.error_msg:
        return web.json_response(_json_error(__api.error_msg))

    data = __db.get_photos(application_settings.token, application_settings.widget_photo_limit)
    photos = InstagramItem.retrieve_list(data)

    response = []
    for photo in photos:
        response.append(photo.convert_to_dict())
    return web.json_response(response)


def _json_error(error_msg):
    return dict(error=str(error_msg))


def start_server(host, port, templates_path, api, db):
    global __api, __db
    __api = api
    __db = db

    templates_directory = Path(__file__).parent.joinpath(templates_path)
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    access_token = application_settings.token
    api = Instagram(access_token)
    db = SqliteDataStorage(application_settings.db_name)
    start_server('127.0.0.1', int('8080'), 'templates/', api, db)
