# query the operating system for information

# python lib imports
from pathlib import Path
import os
# third party imports
# project imports
from settings.reader import read_settings


def get_path_to_(key: str) -> Path:
    """
    fetch keyed path from the system
    :param key: the name/key of the path
    :return: the pathlib.Path path associated with key
    """
    path = get_defined_paths()
    assert key in path, 'unknown path key'
    return path[key]


def get_defined_paths() -> dict:
    """
    fetch all paths as they are defined in the dict instantiation
    :return: a dictionary containing paths keyed by their name
    """
    # define paths
    home = Path(os.environ.get('HOME'))
    project = Path(os.getcwd())
    # fetch path info needed from settings
    app_settings = read_settings(project_root=project)
    data_directory_name = app_settings.get('data_directory_name')
    # assign paths
    path = {
        'home': home,
        'project': project,
        'podcast_backup_data': Path(home, data_directory_name)
    }
    return path
