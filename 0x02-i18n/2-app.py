#!/usr/bin/env python3
""" Flask app module """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Basic config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ function to get the best local language for the request """
    return request.accept_languages.best(app.config(['LANGUAGES']))


@app.route("/")
def index():
    """ main view """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
