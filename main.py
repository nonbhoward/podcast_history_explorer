# the main program sequence

# python lib imports
import os
import pathlib
# third party lib imports
# project imports
from server.data import app_settings
from server.views import app
from settings.reader import read_flask_key_value_from_
from settings.reader import read_settings
from utils.sys_info import build_dict_of_backup_files
from utils.sys_info import build_path_to_data


# project sketch
#   server setup
#     server.data_management initialize objects for server startup
#     server.server initializes routes using objects from
#       server.data_management

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
