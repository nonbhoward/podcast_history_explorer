import os
import pathlib
import yaml
from interface.app_config_editor import init_zip_configuration_in_

# init config location and app_config
config_path = pathlib.Path(os.getcwd(), 'config')
app_config = {}

# init zip configuration
init_zip_configuration_in_(app_config)

# build path to zip configuration
zip_config_file_name = app_config['zip'].get('name')
zip_config_yaml = pathlib.Path(config_path, zip_config_file_name + '.yaml')

# read the configuration
if not os.path.exists(zip_config_yaml):
    raise FileNotFoundError
with open(zip_config_yaml, 'r') as zcy:
    zcf_dict = yaml.load(zcy, Loader=yaml.FullLoader)

# add configuration to app config
app_config['zip']['config'].update(zcf_dict)

# convert lists to paths and build the path
path_root = os.environ.get('HOME')
for name, properties in app_config.items():
    if 'file location' in properties['config']:
        path_segments = properties['config'].get('file location')
        break
    else:
        raise KeyError

path_builder = pathlib.Path(path_root)
for path_segment in path_segments:
    path_builder = pathlib.Path(path_builder, path_segment)
pass
