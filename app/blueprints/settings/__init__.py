from flask import Blueprint

settings = Blueprint(
    "settings", __name__, template_folder="templates", static_folder="static"
)

from . import routes
