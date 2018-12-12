# coding:utf8
from flask import Blueprint

print("__init__")
admin = Blueprint("admin", __name__)


import app.admin.views

