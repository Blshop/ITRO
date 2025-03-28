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


@settings.route("/quality_assuarance")
def quality_assuarance():
    return render_template("settings/quality_assuarance.html")


@settings.route("/periods")
def period():
    return render_template("settings/period.html")


@settings.route("/units")
def unit():
    return render_template("settings/unit.html")


@settings.route("/documents")
def document():
    return render_template("/settings/document.html")


@settings.route("/upload_data", methods=["POST"])
def upload_data():
    data = request.json
    table_name = request.args["table_name"]
    filter = request.args.get("filter", None)

    table_handlers = {
        "deviation": lambda: add_deviation(data),
        "parameter": lambda: add_parameter(data, filter),
        "unit_category": lambda: add_unit_category(data),
        "period": lambda: add_period(data),
        "energy_type": lambda: add_energy_type(data),
        "energy": lambda: add_energy(data),
        "unit_type": lambda: add_unit_type(data),
        "unit": lambda: add_unit(data),
        "document_type": lambda: add_document_type(data),
        "organization": lambda: add_organization(data),
    }
    if table_name in table_handlers:
        try:
            table_handlers[table_name]()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"error": f"Invalid table_name: {table_name}"}), 400


@settings.route("/load_data", methods=["GET"])
def load_data():
    table_name = request.args["table_name"]
    filter = request.args.get("filter", None)
    table_handlers = {
        "deviation": get_deviation,
        "unit_category": get_unit_category,
        "parameter": lambda: get_parameter(filter),
        "period": get_period,
        "energy_type": get_energy_type,
        "energy": get_energy,
        "unit_type": get_unit_type,
        "unit": get_unit,
        "document_type": get_document_type,
        "organization": get_organization,
    }

    try:
        if table_name in table_handlers:
            return jsonify(table_handlers[table_name]())
        else:
            return jsonify({"error": f"Invalid table_name: {table_name}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
