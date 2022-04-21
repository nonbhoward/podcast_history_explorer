# data setup & org to be displayed by the server

# python lib imports
import os
# third party imports
# project imports
from settings.reader import read_settings
from utils.sys_info import build_dict_of_backup_files
from utils.sys_info import build_path_to_data


# local init for server data
#   load settings
app_settings = read_settings()
#   configure logging
#   define data path
path_to_data = build_path_to_data(app_settings=app_settings)
#   read files in the data path, sorted by .. name, date?
backup_files = build_dict_of_backup_files(path_to_data=path_to_data)
#   get a list of the contents of a zip file?
#   unzip a file
#       create a temporary directory for the zip file
#       unzip the contents into the temporary directory
#
#   read available files into metadata


class DataManager:
    def __init__(self):
        # connect instantiated objects to class
        self.app_settings = app_settings
        self.path_to_data = path_to_data
        self.backup_files = backup_files

    def get_file_string(self, line_broken=False) -> str:
        line_break = '<br>' if line_broken else ''
        backup_file_title = f"backup files : {line_break}"
        backup_file_list = ''.join([str(file_path) + line_break for
                                    file_path in self.backup_files])
        return backup_file_title + backup_file_list
