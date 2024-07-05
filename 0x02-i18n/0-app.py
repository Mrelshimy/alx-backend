#!/usr/bin/env python3
""" Flask app module """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """ main view """
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
