import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

FREEZER_DESTINATION = "../"
FREEZER_DESTINATION_IGNORE = ['RyanODonnellResume.pdf', 'README.md', '.git', '.idea', 'blog_app', 'CNAME']
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages, title="Ryan O'Donnell")

@app.route('/blog/')
def blog_index():
    return render_template('blog_index.html', pages=pages,  title="Blog")

@app.route('/blog/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page, title="Blog")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)