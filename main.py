# the main program sequence

# python lib imports
import os
import pathlib
# third party lib imports
# project imports
from server.server import app
from settings.reader import read_flask_key_value_from_
from settings.reader import read_settings
from utils.sys_info import build_dict_of_backup_files
from utils.sys_info import build_path_to_data


# project sketch
# local init
#   load settings
app_settings = read_settings(project_root=os.getcwd())
#   configure logging
#   define data path
path_to_data = build_path_to_data(app_settings=app_settings)
#   read files in the data path, sorted by .. name, date?
backup_files = build_dict_of_backup_files(path_to_data=path_to_data)
#   get a list of the contents of a zip file?
#   unzip a file
#       create a temporary directory for the zip file
#       unzip the contents into the temporary directory

#   read available files into metadata

# server launch
#   fetch server setup
debug = read_flask_key_value_from_(app_settings=app_settings, key='debug')
host = read_flask_key_value_from_(app_settings=app_settings, key='host')
#   set up the server
#   define interface
#     radio list selector
#       unzip, delete,
#       sub-file selector, auto identify type
#         load, view,
#   launch server
app.run(debug=debug, host=host)

# database extras
#   common-query-by-button

# statistical extras
#   (depends on available data)
pass
