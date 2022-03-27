# the main program sequence

# python lib imports
import os
# third party lib imports
from server.server import app
# project imports
from settings.reader import read_flask_debug_value_from_
from settings.reader import read_settings


# project sketch
# local init
#   load settings
app_settings = read_settings(project_root=os.getcwd())
#   configure logging
#   define data path
#   init available file metadata
#   read available files into metadata

# server launch
#   fetch server setup
debug = read_flask_debug_value_from_(app_settings=app_settings)
#   set up the server
#   define interface
#     radio list selector
#       unzip, delete,
#       sub-file selector, auto identify type
#         load, view,
#   launch server
app.run(debug=debug, host='0.0.0.0')

# database extras
#   common-query-by-button

# statistical extras
#   (depends on available data)
pass
