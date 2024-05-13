from flask import Blueprint, render_template, request, redirect, url_for

from functions.settings import (
    add_deviation,
    get_deviations,
    update_deviation,
    add_parameter,
    get_parameters,
    update_parameter,
    add_period,
    get_periods,
    update_period,
    add_unit,
    get_units,
    update_unit,
    add_unit_type,
    get_unit_types,
    update_unit_type
)

settings_bp = Blueprint(
    "settings_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@settings_bp.route("/", methods={"GET", "POST"})
def settings():
    return render_template("settings.html")


@settings_bp.route("/deviations", methods={"GET", "POST"})
def deviation():
    if request.method == "POST":
        if request.form['id'] == "":
            add_deviation(request.form["deviation_desc"])
        else:
            update_deviation(request.form["deviation_desc"], int(request.form['id']))
        return redirect(url_for(".deviation"))
    elif request.method == "GET":
        deviations = get_deviations()
        return render_template(
            "settings/deviation.html",
            deviations=enumerate(deviations),
        )


@settings_bp.route("/parameters", methods=["GET", "POST"])
def parameter(id=None):
    if request.method == "POST":
        if request.form["id"] == "":
            add_parameter(request.form["parameter_desc"], request.form['deviation_desc'])
        else:
            update_parameter(request.form["parameter_desc"], request.form['deviation_desc'],int(request.form['id']))
        return redirect(url_for(".parameter"))
    else:
        parameters = get_parameters()
        deviations = get_deviations()
        return render_template(
            "/settings/parameter.html",
            parameters=enumerate(parameters),
            deviations=deviations,
        )

@settings_bp.route("/periods", methods={"GET", "POST"})
def period():
    if request.method == "POST":
        if request.form['id'] == "":
            add_period(request.form["period_desc"], request.form["period_duration"])
        else:
            update_period(request.form["deviation_desc"], request.form["period_duration"], int(request.form['id']))
        return redirect(url_for(".period"))
    elif request.method == "GET":
        periods = get_periods()
        return render_template(
            "settings/period.html",
            periods=enumerate(periods),
        )
    

@settings_bp.route("/unit_types", methods={"GET", "POST"})
def unit_type():
    if request.method == "POST":
        if request.form['id'] == "":
            add_unit_type(request.form["unit_type_desc"])
        else:
            update_unit_type(request.form["unit_type_desc"], int(request.form['id']))
        return redirect(url_for(".unit_type"))
    elif request.method == "GET":
        unit_types = get_unit_types()
        return render_template(
            "settings/unit_types.html",
            unit_types=enumerate(unit_types),
        )
    

@settings_bp.route("/units", methods={"GET", "POST"})
def unit():
    if request.method == "POST":
        if request.form['id'] == "":
            add_unit(request.form["unit_desc"], request.form["unit_sn"], request.form["unit_type_desc"])
        else:
            update_unit(request.form["unit_desc"], request.form["unit_sn"], int(request.form['id']))
        return redirect(url_for(".unit"))
    elif request.method == "GET":
        units = get_units()
        unit_types = get_unit_types()
        return render_template(
            "settings/unit.html",
            units=enumerate(units),
            unit_types=unit_types
        )