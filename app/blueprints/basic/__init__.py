from flask import Blueprint

basic = Blueprint(
    "basic", __name__, template_folder="templates", static_folder="static"
)

from . import routes
