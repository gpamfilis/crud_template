from flask import Blueprint
api = Blueprint('/', __name__)
from . import views

