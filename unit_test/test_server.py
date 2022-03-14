# unittest for server.server

# python imports
from http.server import HTTPServer
# third party imports
# local imports
from settings.reader import read_settings
from server.server import InterfaceServer
server_class_name = 'InterfaceServer'
test_name = 'test_server'

print(f'START TEST : {test_name}')
# test #0 : test setup, ensure settings loaded
app_settings = read_settings()
assert isinstance(app_settings, dict)

# ensure settings exists for server class
assert server_class_name in app_settings
print(f'\tentry exists for {server_class_name}')

# test #2 : ensure settings entry is saved to server class
interface_server = InterfaceServer(app_settings=app_settings)
assert isinstance(interface_server.settings, dict)
print(f'\t{server_class_name} entry stored in class')

# test #3 : ensure server config has required attributes
required_attributes = ['']

# test #5 : call server, setup, ensure server exists
assert interface_server.server.d is None
print(f'\tserver daemon is None')
interface_server.setup()
assert isinstance(interface_server.server.d, HTTPServer)
print(f'\tserver daemon is {interface_server.server.d}')

# test #6 : start server
# TODO start, check, then stop server

# tests passed
print(f'PASSED TEST : {test_name}')