# unittest for settings.reader

# python imports
# third party imports
# local imports
from settings.reader import read_flask_debug_value_from_
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

# test #2 : ensure flask debug value is set and can be read
app_settings = read_settings()
debug = read_flask_debug_value_from_(app_settings=app_settings)
assert isinstance(debug, bool)
print(f'\tdebug is of bool type')

# tests passed
print(f'PASSED TEST : {test_name}')
