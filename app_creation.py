# -*- coding: utf-8 -*-
"""
_author_    = "Ricardo Lucas"
_copyright_ = "Copyright 2018, ESTIG - IPBeja"
_version_   = "12:58 02/02/2018"
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Creation of Flask Aplication
app = Flask(__name__)

#Load Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uniMadeira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating a SQLAlchemy Object by passing it the application
db = SQLAlchemy(app)