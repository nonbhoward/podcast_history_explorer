import os
import pathlib
import yaml

# initialize
config_path = pathlib.Path(os.getcwd(), 'config')

# fetch zip configuration
app_config = {'zip': {'name': 'zip',
                      'config': {}
                      }}
zip_config_file_name = app_config['zip'].get('name')
zip_config_yaml = pathlib.Path(config_path, zip_config_file_name + '.yaml')
if not os.path.exists(zip_config_yaml):
    raise FileNotFoundError
with open(zip_config_yaml, 'r') as zcy:
    zcf_dict = yaml.load(zcy, Loader=yaml.FullLoader)

app_config['zip']['config'].update(zcf_dict)
