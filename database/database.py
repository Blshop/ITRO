from flask import Blueprint, render_template, request, redirect, url_for, session

from functions.model_functions import (
    add_unit_type,
    get_unit_type,
    edit_unit_type,
    add_period,
    get_period,
    edit_period,
    add_deviation,
    get_deviation,
    edit_deviation,
    add_document_type,
    get_document_type,
    edit_document_type,
    add_source_type,
    get_source_type,
    edit_source_type,
    add_parameter,
    get_parameters,
    edit_parameter,
    add_unit,
    edit_unit,
    get_unit,
)

database_bp = Blueprint(
    "database_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@database_bp.route("/general_data")
def general_data():
    return render_template("database/general_data.html", menu_units=session["units"])


@database_bp.route("general_data/unit_type", methods={"GET", "POST"})
@database_bp.route("general_data/unit_type/<int:id>", methods={"POST"})
def unit_type(id=None):
    if request.method == "POST":
        if request.form["unit_type_desc"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_unit_type(request.form["unit_type_desc"], id)
            else:
                add_unit_type(request.form["unit_type_desc"])
        return redirect(url_for("database_bp.unit_type"))
    elif request.method == "GET":
        unit_types = get_unit_type()
        return render_template(
            "database/general_info/unit_type.html",
            unit_types=unit_types,
            menu_units=session["units"],
        )


@database_bp.route("/general_data/period", methods={"GET", "POST"})
@database_bp.route("/general_data/period/<int:id>", methods={"POST"})
def period(id=None):
    if request.method == "POST":
        if request.form["period_desc"] != "" and request.form["days_number"] > 0:
            if request.form["submit_button"] == "Исправить":
                edit_period(
                    request.form["period_desc"], request.form["days_number"], id
                )
            else:
                add_period(request.form["period_desc"], request.form["days_number"])
        return redirect(url_for("database_bp.period"))
    elif request.method == "GET":
        periods = get_period()
        return render_template(
            "database/general_info/period.html",
            periods=enumerate(periods),
            menu_units=session["units"],
        )


@database_bp.route("/general_data/deviation", methods={"GET", "POST"})
@database_bp.route("/general_data/deviation/<int:id>", methods={"POST"})
def deviation(id=None):
    if request.method == "POST":
        if request.form["submit_button"] == "Исправить":
            edit_deviation(request.form["deviation_value"], id)
        else:
            add_deviation(request.form["deviation_value"])
        return redirect(url_for("database_bp.deviation"))
    elif request.method == "GET":
        deviations = get_deviation()
        return render_template(
            "database/general_info/deviation.html",
            deviations=enumerate(deviations),
            menu_units=session["units"],
        )


@database_bp.route("/general_data/document_type", methods={"GET", "POST"})
@database_bp.route("/general_data/document_type/<int:id>", methods={"POST"})
def document_type(id=None):
    if request.method == "POST":
        if request.form["document_type_desc"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_document_type(request.form["document_type_desc"], id)
            else:
                add_document_type(request.form["document_type_desc"])
        return redirect(url_for("database_bp.document_type"))
    elif request.method == "GET":
        document_types = get_document_type()
        return render_template(
            "database/general_info/document_type.html",
            document_types=enumerate(document_types),
            menu_units=session["units"],
        )


@database_bp.route("/parameter", methods=["GET", "POST"])
@database_bp.route("/parameter/<int:id>", methods={"POST"})
def parameter(id=None):
    if request.method == "POST":
        if request.form["parameter_desc"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_parameter(
                    request.form["parameter_desc"], request.form["deviation_value"], id
                )
            else:
                add_parameter(
                    request.form["parameter_desc"], request.form["deviation_value"]
                )
        return redirect(url_for("database_bp.parameter"))
    else:
        parameters = get_parameters()
        deviations = get_deviation()
        return render_template(
            "/database/parameter.html",
            parameters=enumerate(parameters),
            deviations=deviations,
            menu_units=session["units"],
        )


@database_bp.route("/unit", methods=["GET", "POST"])
@database_bp.route("/unit/<int:id>", methods={"POST"})
def unit(id=None):
    if request.method == "POST":
        if request.form["unit_desc"] != "" and request.form["serial_number"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_unit(
                    request.form["unit_desc"],
                    request.form["serial_number"],
                    request.form["unit_type_desc"],
                    id,
                )
            else:
                add_unit(
                    request.form["unit_desc"],
                    request.form["serial_number"],
                    request.form["unit_type_desc"],
                )
        return redirect(url_for("database_bp.unit"))
    elif request.method == "GET":
        unit_types = get_unit_type()
        units = get_unit()
        print(units)
        return render_template(
            "database/unit.html",
            menu_units=session["units"],
            units=enumerate(units),
            unit_types=unit_types,
        )


@database_bp.route("general_data/source_type", methods={"GET", "POST"})
@database_bp.route("general_data/source_type/<int:id>", methods={"POST"})
def source_type(id=None):
    if request.method == "POST":
        if request.form["source_type_desc"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_source_type(request.form["source_type_desc"], id)
            else:
                add_source_type(request.form["source_type_desc"])
        return redirect(url_for("database_bp.source_type"))
    elif request.method == "GET":
        source_types = get_source_type()
        return render_template(
            "database/general_info/source_type.html",
            source_types=source_types,
            menu_units=session["units"],
        )


@database_bp.route("/source_energy", methods=["GET", "POST"])
@database_bp.route("/source_energy/<int:id>", methods={"POST"})
def source_energy(id=None):
    if request.method == "POST":
        if request.form["source_energy_desc"] != "":
            if request.form["submit_button"] == "Исправить":
                edit_parameter(
                    request.form["source_energy_desc"],
                    request.form["deviation_value"],
                    id,
                )
            else:
                add_parameter(
                    request.form["source_energy_desc"], request.form["deviation_value"]
                )
        return redirect(url_for("database_bp.source_energy"))
    else:
        source_energies = get_parameters()
        deviations = get_deviation()
        return render_template(
            "/database/source_energy.html",
            source_energies=enumerate(source_energies),
            deviations=deviations,
            menu_units=session["units"],
        )
