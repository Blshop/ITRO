from flask import Blueprint, render_template, request, redirect, url_for, session, json

from functions.settings import get_periods
from functions.settings import get_units, get_unit
from functions.unit import prepare_unit_parameters, print_period_parameters


documents_bp = Blueprint(
    "documents_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@documents_bp.route("/protocols", methods={"GET", "POST"})
def protocols():
    periods = get_periods()
    units = get_units()
    return render_template("documents/protocols.html", periods=periods, units=units)


@documents_bp.route("/print", methods=["GET", "POST"])
def print_parameters():
    if request.method == "POST":
        print(request.json)
        session["to_print"] = request.json["data"]
        session["date"] = request.json["date"]
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    else:
        to_print = print_period_parameters(session["to_print"])
        return render_template(
            "documents/print_daily.html",
            to_print=to_print,
            date=session["date"].split("-"),
        )


@documents_bp.route("/documents", methods={"GET", "POST"})
def documents():
    periods = get_periods()
    units = get_units()
    return render_template("documents/protocols.html", periods=periods, units=units)
