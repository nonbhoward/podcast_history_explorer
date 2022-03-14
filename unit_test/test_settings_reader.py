# unittest for settings.reader
from settings.reader import read_settings
# declare path to settings, open in read-mode, load the file, assert
test_name = 'test_settings_reader'
print(f'START TEST : {test_name}')
app_settings = read_settings()
print(f'\tapp_settings = {app_settings}')
assert isinstance(app_settings, dict)
print(f'PASSED TEST : {test_name}')
