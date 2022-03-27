# unittest for settings.reader

# python imports
# third party imports
# local imports
from settings.reader import read_flask_key_value_from_
from settings.reader import read_settings
test_name = 'test_settings_reader'

# tests start
print(f'START TEST : {test_name}')

# test #0 : test setup, none

# test #1 : ensure test setup, declare path to settings, open in read-mode,
#   load the file, assert
app_settings = read_settings()
assert isinstance(app_settings, dict)
print(f'\tsettings is of dictionary type')

# test #2 : ensure flask key values are set and can be read
key = 'debug'
debug = read_flask_key_value_from_(app_settings=app_settings, key=key)
assert isinstance(debug, bool)
print(f'\t{key} is of bool type')

key = 'host'
host = read_flask_key_value_from_(app_settings=app_settings, key=key)
assert isinstance(host, str)
print(f'\t{key} is of str type')

# tests passed
print(f'PASSED TEST : {test_name}')
