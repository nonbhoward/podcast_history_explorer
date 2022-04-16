# the main program sequence

# python lib imports
import os
import pathlib
# third party lib imports
# project imports
from server.server import app
from settings.reader import read_flask_key_value_from_
from settings.reader import read_settings
from utils.sys_info import build_path_to_data


# project sketch
# local init
#   load settings
app_settings = read_settings(project_root=os.getcwd())
#   configure logging
#   define data path
path_to_data = build_path_to_data(app_settings=app_settings)
#   init available file metadata
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
