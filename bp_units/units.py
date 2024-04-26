from flask import Blueprint, render_template, request, redirect, url_for, session
from functions.settings import get_parameters, get_periods
from functions.unit import add_unit_parameter, prepare_unit_parameters


units_bp = Blueprint(
    "units_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@units_bp.route("/<variable>", methods=["GET", "POST"])
def unit(variable):
    session['current_unit'] = variable
    return render_template("unit.html")


@units_bp.route("/unit_parameter", methods=["GET", "POST"])
def unit_parameter():
    if request.method == "POST":
        add_unit_parameter(session['current_unit'], request.form['parameter_desc'], request.form['period_desc'])
        return redirect(url_for(".unit_parameter"))
    else:
        parameters = get_parameters()
        periods = get_periods()
        result = prepare_unit_parameters(session['current_unit'])

        return render_template("units/unit_parameter.html", parameters=parameters, periods=periods, result=result)


@units_bp.route("/print", methods=["GET", "POST"])
def print_parameters():
    unit_parameters = prepare_unit_parameters(session['current_unit'])
    return render_template("units/print_parameters.html", unit_parameters=unit_parameters)