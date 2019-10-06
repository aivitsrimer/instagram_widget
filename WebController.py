from pathlib import Path

from aiohttp import web
import aiohttp_jinja2
import jinja2

from WebApplication.CollectionManager import CollectionManager
from WebApplication.DataStorage import DataStorage


routes = web.RouteTableDef()


def __get_collection_storage(request: web.Request, name: str) -> DataStorage:
    manager: CollectionManager = request.app['collection_manager']
    return manager.data_storage(name)


@routes.get('/')
async def root(_request: web.Request) -> web.Response:
    raise web.HTTPFound(location='/collections')


@routes.get('/collections')
@aiohttp_jinja2.template('collections.jinja2')
async def collections(request: web.Request) -> dict:
    manager: CollectionManager = request.app['collection_manager']
    return {'collections': manager.collections()}


@routes.get('/collection/{collection}')
@aiohttp_jinja2.template('collection.jinja2')
async def collection(request: web.Request) -> dict:
    name = request.match_info['collection']
    storage: DataStorage = __get_collection_storage(request, name)

    return {'name': name, 'collection': list(storage.get_objects())}


@routes.post('/collection/{collection}/add')
async def put_object(request: web.Request) -> web.Response:
    data = await request.post()

    name = request.match_info['collection']
    storage: DataStorage = __get_collection_storage(request, name)

    storage.put_object(data['original'], {
        'translation': data['translation'],
        'transcription': data['transcription'],
    })

    return web.HTTPFound(location=f'/collection/{name}')


@routes.get('/api/collections')
async def collections(request: web.Request) -> web.Response:
    manager: CollectionManager = request.app['collection_manager']
    return web.json_response(manager.collections())


@routes.get('/api/collection/{collection}')
async def collection(request: web.Request) -> web.Response:
    manager: CollectionManager = request.app['collection_manager']
    storage: DataStorage = manager.data_storage(request.match_info['collection'])

    return web.json_response(list(storage.get_objects()))


@routes.get('/api/collection/{collection}/{object}')
async def get_object(request: web.Request) -> web.Response:
    storage: DataStorage = __get_collection_storage(request, request.match_info['collection'])
    return web.json_response(storage.get_object(request.match_info['object']))


@routes.post('/api/collection/{collection}')
async def put_object(request: web.Request) -> web.Response:
    data = await request.json()

    storage: DataStorage = __get_collection_storage(request, request.match_info['collection'])
    storage.put_object(data.pop('original'), data)

    return web.Response(status=web.HTTPOk.status_code)


@routes.delete('/api/collection/{collection}/{object}')
def delete_object(request: web.Request) -> web.Response:
    storage: DataStorage = __get_collection_storage(request, request.match_info['collection'])
    storage.delete_object(request.match_info['object'])

    return web.Response(status=web.HTTPOk.status_code)


if __name__ == '__main__':
    settings = {
        'port': 8080,
        'data_directory': Path(__file__).parent.parent
    }

    templates_directory = Path(__file__).parent.joinpath('templates')

    app = web.Application()
    app['collection_manager'] = CollectionManager(settings['data_directory'])

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    web.run_app(app, port=settings['port'])
