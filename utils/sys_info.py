# utilities to get information from the operating system

# python lib imports
import copy
import os
import pathlib
# third party imports
# project imports


def build_dict_of_backup_files(path_to_data) -> dict:
    """
    initialize and populate the dictionary of file data
    :param path_to_data: the location to search for files
    :return: files that meet the requirements of a backup file
    """
    if not os.path.exists(path_to_data):
        print(f'path does not exist: {path_to_data}, will now exit')
        exit()
    all_files = get_all_files_from(path_to_data)
    backup_files = filter_backup_files_from(all_files)
    return backup_files


def build_path_to_data(app_settings) -> pathlib.Path:
    """
    using app_settings to define the data directory name, build the path
      to the location of the backup files containing the data of interest
    :param app_settings: a dictionary containing the app configuration
    :return: a path to the backup files
    """
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


def get_all_files_from(path_to_data) -> dict:
    """
    read all files in the backup directory and ensure at least one
      entry is found, otherwise end the program
    :param path_to_data: the location of the backup data
    :return: a dictionary of all files in the backup directory
    """
    all_files = {}
    for root, _, files in os.walk(path_to_data):
        for file in files:
            path_to_file = pathlib.Path(root, file)
            file_details = {
                'extension': get_extension_from(path_to_file)
            }
            all_files[path_to_file] = {}
            all_files[path_to_file].update({
                'details': file_details
            })
    if not all_files:
        print(f'failed to locate any files in directory, will now exit')
        exit()
    return all_files


def get_extension_from(path_to_file: pathlib.Path) -> str:
    """
    strip the extension from the end of a file path
    :param path_to_file: the path to a file on the system
    :return: a file extension, or an empty string if no extension is found
    """
    path_to_file_as_string = str(path_to_file)
    if '.' not in path_to_file_as_string:
        return ''  # no extension
    extension = path_to_file_as_string.split('.')[-1]
    return extension


def filter_backup_files_from(all_files) -> dict:
    """
    discord files that are not backup files
    :param all_files: a dictionary of file data
    :return: a dictionary of backup file data
    """
    mutable_all_files = copy.deepcopy(all_files)
    backup_extensions = ['zip']
    for file_path, data in all_files.items():
        if data['details']['extension'] not in backup_extensions:
            mutable_all_files.pop(file_path)
    return mutable_all_files
