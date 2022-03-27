# unittest for content.link

# python imports
import html.parser
# third party imports
# local imports
from content.link import Endpoint
from server.server import __all__ as server_functions
test_name = 'test_content_link'

# tests start
print(f'START TEST : {test_name}')

# test #0 : test setup, none

# test #1 : ensure each content endpoint has a server function
for server_function in server_functions:
    print(f'\tchecking {server_function}')
    found_name = []
    for endpoint_name in Endpoint.all_point_names:
        print(f'\t\tcheck if {endpoint_name} in {server_function}')
        found_name.append(endpoint_name in server_function)
    assert any(found_name)

# tests passed
print(f'PASSED TEST : {test_name}')
