import os
from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.owners.views import owners_blueprint
from myproject.puppies.views import puppies_blueprint

app.register_blueprint(owners_blueprint,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
