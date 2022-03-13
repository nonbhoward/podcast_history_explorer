# read the project settings file

# python lib imports
import os
import pathlib
# third party imports
import yaml
settings_directory = 'settings'
settings_filenames = 'settings.yaml'


def read_settings(project_root=pathlib.Path(os.getcwd()).parent,
                  directory='settings',
                  filename='settings.yaml') -> dict:
    """
    open settings file in read-mode, load the file
    :param project_root: name of settings directory
    :param directory: name of settings directory
    :param filename: name of settings file
    :return: dictionary containing settings
    """
    path_to_settings = pathlib.Path(project_root, directory, filename)
    with open(path_to_settings, 'r') as settings:
        app_settings = yaml.safe_load(settings)
    return app_settings


def test_settings_reader():
    name = 'test_settings_reader'
    """
    declare path to settings, open in read-mode, load the file, assert
      loaded file is expected type
    :return:
    """
    print(f'START TEST : {name}')
    app_settings = read_settings()
    print(f'\tapp_settings = {app_settings}')
    assert isinstance(app_settings, dict)
    print(f'PASSED TEST : {name}')


if __name__ == '__main__':
    test_settings_reader()
