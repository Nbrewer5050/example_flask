#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Flask init"""

from flask import Flask # from the flask module import the Flask class
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = "some hard to guess string"

from app import routes
