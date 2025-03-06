from flask import render_template, request, jsonify
from . import settings
from app.services.settings import (
    add_deviation,
    get_deviation,
    add_unit_category,
    get_unit_category,
    add_parameter,
    get_parameter,
    add_period,
    get_period,
    get_energy_type,
    add_energy_type,
    get_energy,
    add_energy,
    add_unit,
    get_unit,
    add_unit_type,
    get_unit_type,
    get_document_type,
    add_document_type,
    get_organization,
    add_organization,
)


@settings.route("/quality_assuarance", methods={"GET"})
def quality_assuarance():
    return render_template("settings/quality_assuarance.html")


@settings.route("/periods", methods={"GET", "POST"})
def period():
    return render_template("settings/period.html")


@settings.route("/units", methods={"GET", "POST"})
def unit():
    return render_template("settings/unit.html")


@settings.route("/documents", methods=["GET", "POST"])
def document():
    return render_template("/settings/document.html")


@settings.route("/upload_data", methods=["POST"])
def upload_data():
    data = request.json
    table_name = request.args["table_name"]
    filter = request.args.get("filter", None)
    if table_name == "deviation":
        add_deviation(data)
    elif table_name == "parameter":
        add_parameter(data, filter)
    elif table_name == "unit_category":
        add_unit_category(data)
    elif table_name == "period":
        add_period(data)
    elif table_name == "energy_type":
        add_energy_type(data)
    elif table_name == "energy":
        add_energy(data)
    elif table_name == "unit_type":
        add_unit_type(data)
    elif table_name == "unit":
        add_unit(data)
    elif table_name == "document_type":
        add_document_type(data)
    elif table_name == "organization":
        add_organization(data)
    return jsonify({})


@settings.route("/load_data", methods=["GET"])
def load_data():
    table_name = request.args["table_name"]
    filter = request.args.get("filter", None)
    if table_name == "deviation":
        return jsonify(get_deviation())
    elif table_name == "unit_category":
        return jsonify(get_unit_category())
    elif table_name == "parameter":
        return jsonify(get_parameter(filter))
    elif table_name == "period":
        return jsonify(get_period())
    elif table_name == "energy_type":
        return jsonify(get_energy_type())
    elif table_name == "energy":
        return jsonify(get_energy())
    elif table_name == "unit_type":
        return jsonify(get_unit_type())
    elif table_name == "unit":
        return jsonify(get_unit())
    elif table_name == "document_type":
        return jsonify(get_document_type())
    elif table_name == "organization":
        return jsonify(get_organization())
