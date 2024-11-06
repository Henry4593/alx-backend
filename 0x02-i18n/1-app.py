#!/usr/bin/env python3
"""
Flask application with Babel for i18n support.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask application.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel: Babel = Babel(app)


@app.route('/')
def main() -> str:
    """
    Render the main page of the application.

    Returns:
        str: The rendered template for the main page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
