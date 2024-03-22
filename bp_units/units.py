from flask import Blueprint, render_template, request, redirect, url_for, session
from functions.settings import get_parameters


units_bp = Blueprint(
    "units_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@units_bp.route("/unit/<variable>", methods=["GET", "POST"])
def unit(variable):
    session['current_unit'] = variable
    return render_template("unit.html")


@units_bp.route("/unit_parameter")
def unit_parameter():
    parameters = get_parameters()
    return render_template("units/unit_parameter.html", parameters=parameters)

