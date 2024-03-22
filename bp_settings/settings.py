from flask import Blueprint, render_template, request, redirect, url_for, session

from functions.model_functions import (
    get_source_types,
    add_x_ray,
    get_x_rays,
    add_photon,
    get_photons,
    add_electron,
    get_electrons,
    add_isotope,
    get_isotopes,
    add_unit_type,
    get_unit_type,
    edit_unit_type,
    add_period,
    get_period,
    edit_period,
    add_document_type,
    get_document_type,
    edit_document_type,
    add_source_type,
    get_source_type,
    edit_source_type,
)
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
        if request.form['id'] is "":
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
        if request.form["id"] is "":
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
        if request.form['id'] is "":
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
    

@settings_bp.route("/units", methods={"GET", "POST"})
def unit():
    if request.method == "POST":
        if request.form['id'] is "":
            add_unit(request.form["unit_desc"], request.form["unit_sn"])
        else:
            update_unit(request.form["dunit_desc"], request.form["unit_sn"], int(request.form['id']))
        return redirect(url_for(".unit"))
    elif request.method == "GET":
        units = get_units()
        return render_template(
            "settings/unit.html",
            units=enumerate(units),
        )


@settings_bp.route("energies", methods={"GET", "POST"})
def energies():
    if request.method == "POST":
        form = request.args.get("f")
        match form:
            case "x_rays":
                add_x_ray(request.form["voltage"], request.form["current"])
            case "photons":
                add_photon(request.form["photon_desc"])
            case "electrons":
                add_electron(request.form["electron_desc"])
            case "isotopes":
                add_isotope(request.form["isotope_desc"], request.form["half_life"])
        return redirect(url_for("equipment_data_bp.energies"))
    elif request.method == "GET":
        data = {}
        data["source_types"] = get_source_types()
        data["x_rays"] = get_x_rays()
        data["photons"] = get_photons()
        data["electrons"] = get_electrons()
        data["isotopes"] = get_isotopes()
        return render_template("equipment_data/energies.html", data=data)


@settings_bp.route("acessories", methods={"GET", "POST"})
def acessories():
    if request.method == "POST":
        if request.form["period_desc"] != "" and request.form["days_number"] > 0:
            if request.form["submit_button"] == "Исправить":
                edit_period(
                    request.form["period_desc"], request.form["days_number"], id
                )
            else:
                add_period(request.form["period_desc"], request.form["days_number"])
        return redirect(url_for("database_bp.acessories"))
    elif request.method == "GET":
        return render_template("equipment_data/acessories.html")


@settings_bp.route("/general_data/document_type", methods={"GET", "POST"})
@settings_bp.route("/general_data/document_type/<int:id>", methods={"POST"})
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


@settings_bp.route("general_data/source_type", methods={"GET", "POST"})
@settings_bp.route("general_data/source_type/<int:id>", methods={"POST"})
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


@settings_bp.route("/source_energy", methods=["GET", "POST"])
@settings_bp.route("/source_energy/<int:id>", methods={"POST"})
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
