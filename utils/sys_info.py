# utilities to get information from the operating system

# python lib imports
import os
import pathlib
# third party imports
# project imports


def build_path_to_data(app_settings) -> pathlib.Path:
    key = 'data_directory_name'
    data_directory_name = app_settings.get(key, '')
    if not data_directory_name:
        print(f'app_settings missing key: {key}, will now exit')
        exit()
    key = 'HOME'
    home = os.environ.get(key, '')
    if not home:
        print(f'environment variable {key} not found, will now exit')
        exit()
    path_to_data = pathlib.Path(home, data_directory_name)
    return path_to_data
