# the main program sequence

# python lib imports
import os
# third party lib imports
from flask import Flask
# project imports
from content.content import start_page
from settings.reader import read_settings
app = Flask(__name__)


@app.route('/')
def app_root():
    return start_page


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
#   define interface
#     radio list selector
#       unzip, delete,
#       sub-file selector, auto identify type
#         load, view,
#   launch server
app.run(debug=True, host='0.0.0.0')

# database extras
#   common-query-by-button

# statistical extras
#   (depends on available data)
pass
