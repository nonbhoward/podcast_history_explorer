# the main program sequence

# python lib imports
import os
# third party lib imports
# project imports
from server.server import PodcastApplication
from settings.reader import read_flask_key_value_from_
from settings.reader import read_settings


# project sketch
# local init
#   load settings
app_settings = read_settings(project_root=os.getcwd())

# server launch
#   fetch server setup values
debug = read_flask_key_value_from_(app_settings=app_settings, key='debug')
host = read_flask_key_value_from_(app_settings=app_settings, key='host')
#   launch server
PodcastApplication.run(debug=debug,
                       host=host)

# database extras
#   common-query-by-button

# statistical extras
#   (depends on available data)
pass
