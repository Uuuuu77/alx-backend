#!/usr/bin/env python3

""" Basic Babel setup """

from flask import Flask, render_template
from flask_babel import Babel

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """ Language configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ Index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
