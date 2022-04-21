# unittest for content.link

# python imports
import html.parser
# third party imports
# local imports
from content.link import Endpoint
from server.views import __all__ as server_views
test_name = 'test_content_link'

# tests start
print(f'START TEST : {test_name}')

# test #0 : test setup, none

# test #1 : ensure each content endpoint has a server function
for server_view in server_views:
    print(f'\tchecking {server_view}')
    found_name = []
    for endpoint_name in Endpoint.all_point_names:
        print(f'\t\tcheck if {endpoint_name} in {server_view}')
        found_name.append(endpoint_name in server_view)
    assert any(found_name)

# tests passed
print(f'PASSED TEST : {test_name}')
