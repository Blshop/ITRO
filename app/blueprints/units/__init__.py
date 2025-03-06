from flask import Blueprint

units = Blueprint(
    "units", __name__, template_folder="templates", static_folder="static"
)

from . import routes
