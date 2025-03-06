from flask import Blueprint

documents = Blueprint(
    "documents", __name__, template_folder="templates", static_folder="static"
)

from . import routes
