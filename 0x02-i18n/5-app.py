#!/usr/bin/env python3

""" Mock logging in """

from flask import Flask, render_template, g, request
from flask_babel import Babel, _

app: Flask = Flask(__name__)
babel: Babel = Babel(app)

users: dict = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    """ Gets a user """
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """ Before request """
    user_id: int = int(request.args.get('login_as', 0))
    g.user: dict = get_user(user_id) if user_id else None


@app.route('/')
def index() -> str:
    """ Index page """
    if g.user:
        welcome_message: str = (
                _(
                    "You are logged in as %(username)s."
                ) % {'username': g.user['name']}
        )
    else:
        welcome_message: str = _("You are not logged in.")
    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
