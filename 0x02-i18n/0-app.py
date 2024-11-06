#!/usr/bin/env python3
"""
This module contains a simple Flask application.
"""
from flask import Flask, render_template
from typing import Any, Optional


app: Flask = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def main() -> str:
    """
    Renders the main page of the application.

    Returns:
        The rendered template for the main page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
