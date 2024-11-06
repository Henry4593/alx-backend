#!/usr/bin/env python3
"""
This module contains a Flask application configured with Babel for
internationalization (i18n) support.
"""
from flask_babel import Babel, format_datetime
import pytz
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel: Babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieve the user based on the 'login_as' query parameter.

    Returns:
        Union[Dict, None]: The user dictionary if found, otherwise None.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """
    Function to be executed before each request.
    Sets the global user object.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.

    Returns:
        str: The best match language code.
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_locale() -> str:
    """
    Determines the appropriate timezone for the user.

    This function attempts to retrieve the timezone from the request arguments.
    If not found, it checks if the user is logged in and retrieves the user's
    timezone. If the timezone is invalid or not found, it returns the default
    timezone from the application configuration.

    Returns:
        str: The valid timezone string or the default timezone.
    """
    timezone = request.args.get('timezone', '')
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def main() -> str:
    """
    Render the main page of the application.

    Returns:
        str: The rendered template for the main page.
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
