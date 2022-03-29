# python lib imports
from pathlib import Path
import os
# third party imports
from flask import Flask
from flask import url_for
# project imports
from content.link import Endpoint
from content.style import CSS
from util.get_sys_info import get_path_to_
app = Flask(__name__)
endpoints = ['fl_root', 'fl_branch']
__all__ = ['fl_root', 'fl_testing']
acceptable_file_extensions = ['zip']


class PodcastApplication(app):
    def __init__(self, path_to_backup_data: Path,
                 use_cache=False):
        # init default values
        self._cache_valid = False  # data validation indicator
        self._cache = None  # still valid data from previous runs
        self._backup_files = []  # a list of backup file paths
        # assign values
        self._cache_in_use = use_cache
        if not path_to_backup_data:
            self._path_to_backup_data = get_path_to_('podcast_backup_data')
        # project sketch
        #   configure logging
        #   DONE: define data path
        #   init available file metadata
        if self._cache_in_use:
            self.check_cache()
        if self._cache_valid:
            self.load_cache()
            return
        #   read available files into metadata
        self.validate_backup_files()
        if not self._backup_files:
            assert self._backup_files, "no backup files were found in data " \
                                       "directory"
            return
        #   decompress the backup files
        #   identify each decompressed file
        #   evaluate each decompressed file
        #   store evaluated file data in class
        #   set up the server
        #   define interface
        #     radio list selector
        #       unzip, delete,
        #       sub-file selector, auto identify type
        #         load, view,
        # super() class doesn't need to initialize

    def check_cache(self):
        """
        check to see if there exists a valid cache
        TODO
        :return:
        """
        self._cache_valid = False

    def load_cache(self):
        """
        load the cache data into the class
        TODO
        :return:
        """
        self._cache = None

    def validate_backup_files(self):
        """
        :return:
        """
        backup_files = []
        path_to_data = self._path_to_backup_data
        for root, _, files in os.walk(path_to_data):
            for file in files:
                file_ext = file.split('.')[-1]
                if file_ext in acceptable_file_extensions:
                    backup_files.append(Path(root, file))
        self._backup_files = backup_files


@PodcastApplication.route('/hello/<name>')
def fl_hello(name):
    """
    testing endpoint
    :return:
    """
    return f"""
    {CSS.center_below}
    {Endpoint.root}<br>
    {Endpoint.branch}<br>
    hello {name}
    {CSS.center_above}
    <br>"""


@PodcastApplication.route('/')
def fl_root():
    """
    site root
    :return:
    """
    path_to_podcast_backups = get_path_to_('podcast_backup_data')
    return f"""
    {CSS.center_below}
    this is root<br>
    podcast backup data is located: {path_to_podcast_backups}<br>
    {CSS.center_above}
    """


@PodcastApplication.route('/testing')
def fl_testing():
    """
    testing endpoint
    :return:
    """
    return f"""
    {CSS.center_below}
    {Endpoint.root}<br>
    testing<br>
    {Endpoint.hello}<br>
    {CSS.center_above}
    """


def _print_urls():
    """
    print url per endpoint
    :return:
    """
    with PodcastApplication.test_request_context():
        for endpoint in endpoints:
            print(url_for(endpoint))


if __name__ == '__main__':
    _print_urls()
else:
    print(f'importing {__name__}')
