# page routing for the flask server

# python lib imports
import os
# third party imports
from flask import Flask
from flask import url_for
# project imports
from content.link import Endpoint
from content.style import CSS

app = Flask(__name__)
endpoints = ['fl_root', 'fl_branch']
__all__ = ['fl_root', 'fl_testing']


@app.route('/')
def fl_root():
    """
    site root
    :return:
    """
    return f"""
    {CSS.center_below}
    this is root<br>
    the cwd is {cwd}<br>
    {CSS.center_above}
    """


@app.route('/testing')
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


@app.route('/hello/<name>')
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


@app.route('/print/path/data')
def fl_print_path_to_data():
    pass


def _print_urls():
    """
    print url per endpoint
    :return:
    """
    with app.test_request_context():
        for endpoint in endpoints:
            print(url_for(endpoint))


if __name__ == '__main__':
    _print_urls()
else:
    print(f'importing {__name__}')
