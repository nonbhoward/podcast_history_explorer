# unittest for settings.reader

# python imports
# third party imports
# local imports
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

# tests passed
print(f'PASSED TEST : {test_name}')
