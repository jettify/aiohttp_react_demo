import os
import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web


@aiohttp_jinja2.template('index.html')
@asyncio.coroutine
def index(request):
    title = 'Aiohttp Debugtoolbar'
    # log.info(title)

    return {
        'title': title,
        'show_jinja2_link': True,
        'show_sqla_link': False,
        'app': request.app}


@aiohttp_jinja2.template('hello.html')
@asyncio.coroutine
def hello(request):
    title = 'Aiohttp Debugtoolbar'
    # log.info(title)

    return {
        'title': title,
        'show_jinja2_link': True,
        'show_sqla_link': False,
        'app': request.app}


project_root = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(project_root, 'templates')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(project_root))

    app.router.add_static('/static', os.path.join(project_root, 'static'))

    app.router.add_route('GET', '/', index, name='index')
    app.router.add_route('GET', '/hello', hello, name='hello')


    handler = app.make_handler()
    srv = yield from loop.create_server(handler, '127.0.0.1', 9000)
    print("Server started at http://127.0.0.1:9000")
    return srv, handler


loop = asyncio.get_event_loop()
srv, handler = loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(handler.finish_connections())

