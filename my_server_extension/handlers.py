from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.serverapp import ServerApp
from tornado.web import authenticated


def _load_jupyter_server_extension(serverapp: ServerApp):
    """
    This function is called when the extension is loaded.
    """
    handlers = [
        ("/myextension/hello", MyExtensionHandler)
    ]
    serverapp.web_app.add_handlers(".*$", handlers)


class MyExtensionHandler(JupyterHandler):

    @authenticated
    async def get(self):
        self.finish("Hello World!")
