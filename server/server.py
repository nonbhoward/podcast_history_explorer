# launch the interface server
from http.server import HTTPServer


class InterfaceServer:
    # manage objects related to the interface server
    def __init__(self, app_settings):
        self._app_settings = app_settings
        self.settings = app_settings.get('InterfaceServer', None)
        self.server = HTTPServer
        pass

    @property
    def app_settings(self):
        return self._app_settings

    @app_settings.setter
    def app_settings(self, value):
        print(f'do not set {self.__class__.__name__}._app_settings')

    def setup(self):
        pass

    def start(self):
        self.setup()
        pass


if __name__ == '__main__':
    pass
else:
    print(f'importing {__name__}')
