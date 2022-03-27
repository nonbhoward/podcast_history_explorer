from content.content import branch
from content.content import hello
from content.content import root
from flask import Flask
from flask import url_for
app = Flask(__name__)
endpoints = ['fl_root', 'fl_branch']


@app.route('/')
def fl_root():
    return root


@app.route('/branch')
def fl_branch():
    return branch


@app.route('/hello/<name>')
def fl_hello(name):
    return f'{hello} {name}'


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
