from flask import render_template, session
from . import basic
from app.services.settings import get_unit


@basic.route("/", methods={"GET"})
def index():
    session.clear()
    session["main_units"] = get_unit("основные")
    session["sec_units"] = get_unit("вторичные")
    session["planning"] = get_unit("планирование")
    return render_template("index.html")
