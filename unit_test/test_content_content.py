# unittest for content.content

# python imports
import html.parser
# third party imports
# local imports
from content.content import branch
from content.content import hello
from content.content import root
test_name = 'test_content_content'

# tests start
print(f'START TEST : {test_name}')

# test #0 : test setup, none

# test #1 : ensure html is str
assert isinstance(branch, str)
print(f'\t{branch} is of str type')
assert isinstance(hello, str)
print(f'\t{hello} is of str type')
assert isinstance(root, str)
print(f'\t{root} is of str type')

# tests passed
print(f'PASSED TEST : {test_name}')
