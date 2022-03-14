# launch the interface server
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class InterfaceServer:
    # manage objects related to the interface server
    class Server:
        # manage objects related to server
        d = None  # daemon

    def __init__(self, app_settings):
        # load settings
        self._app_settings = app_settings
        self.settings = app_settings.get('InterfaceServer', None)

        # init variables
        self.server = self.Server()
        self.host = None
        self.port = None
        self.handler = None

    @property
    def app_settings(self):
        return self._app_settings

    @app_settings.setter
    def app_settings(self, value):
        print(f'do not set {self.__class__.__name__}._app_settings')

    def setup(self, handler=BaseHTTPRequestHandler):
        """
        instantiate the http server
        :param handler: required argument for HTTPServer
          provides a number of class or instance variables, and methods used by
          subclasses. used to handle requests that arrive at the server. alone,
          it cannot respond to any actual HTTP requests and must be subclassed
          to handle each request method (GET, POST)
          the handler will parse the request and headers,then call the method
          specific to the request type. the method name is constructed from
          the request
          example :
            for request method SPAM, do_SPAM() method will be called with no
              arguments.
          all the relevant information is stored in instance variables of the
            handler
        :return:
        """
        # instantiate the server
        host = self.settings.get('host', None)
        port = self.settings.get('port', None)
        # HTTPServer is a socketserver.TCPServer subclass
        self.server.d = HTTPServer(server_address=(host, port),
                                   RequestHandlerClass=handler)
        # after successful instantiation, save to class
        self.host = host
        self.port = port

    def start(self):
        """
        start the server
        :return:
        """
        # TODO


if __name__ == '__main__':
    pass
else:
    print(f'importing {__name__}')
