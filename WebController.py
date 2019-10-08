from pathlib import Path

import jinja2
from aiohttp import web
import aiohttp_jinja2

from InstagramItem import InstagramItem
from Instagram import Instagram

from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage


routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('main_page.jinja2')
async def main_page(request: web.Request):
    pass


@routes.get('/widget')
@aiohttp_jinja2.template('widget.jinja2')
async def widget(request: web.Request):
    name = 'Photos'
    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(application_settings.token)
    photos = InstagramItem.retrieve_list(data)

    return {'name': name, 'photos': photos}


@routes.get('/api/media')
async def api_media(request: web.Request) -> web.Response:
    api = Instagram(application_settings.token)
    return web.json_response(api.media())


@routes.get('/api/widget')
async def api_widget(request: web.Request) -> web.Response:
    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(application_settings.token)
    photos = InstagramItem.retrieve_list(data)
    response = []
    for photo in photos:
        response.append(photo.convert_to_dict())
    return web.json_response(response)


def start_server(host, port, templates_path):

    templates_directory = Path(__file__).parent.joinpath(templates_path)
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    start_server('127.0.0.1', int('8080'), 'templates/')
