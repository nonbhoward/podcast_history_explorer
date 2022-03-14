# the main program sequence

# python lib imports
import os
# third party lib imports
# project imports
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
#   setup the server
if_server = InterfaceServer(app_settings=app_settings)
if_server.setup()
#   define interface
#     radio list selector
#       unzip, delete,
#       sub-file selector, auto identify type
#         load, view,
#   launch server
if_server.start()

# database extras
#   common-query-by-button

# statistical extras
#   (depends on available data)
pass
