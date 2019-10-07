from pathlib import Path

import jinja2
from aiohttp import web
import aiohttp_jinja2

from InstagramItem import InstagramItem

from ApplicationSettings import application_settings
from SqliteDataStorage import SqliteDataStorage


routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('main_page.jinja2')
async def collections(request: web.Request):
    print(request.url.relative())
    # возможность перехода на виджет и json


@routes.get('/widget')
@aiohttp_jinja2.template('widget.jinja2')
async def get_photos(request: web.Request):
    name = 'Photos'
    db = SqliteDataStorage(application_settings.db_name)
    data = db.get_photos(application_settings.token)
    photos = InstagramItem.retrieve_list(data)

    return {'name': name, 'photos': photos + photos}
    # отображение фото из InstagramItem


# @routes.get('/api/json')
# async def collections(request: web.Request) -> web.Response:
#     manager: CollectionManager = request.app['collection_manager']
#     return web.json_response(manager.collections())
#     # вывести json

def start_server(host, port, templates_path):

    templates_directory = Path(__file__).parent.joinpath(templates_path)
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    start_server('127.0.0.1', int('8080'), 'templates/')
