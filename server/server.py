from content.content import branch
from content.content import start_page
from flask import Flask
app = Flask(__name__)


@app.route('/')
def site_root():
    return start_page


@app.route('/branch')
def branch():
    return branch
