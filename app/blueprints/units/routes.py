from flask import render_template, session, redirect, request, url_for, jsonify, json
from . import units
import os
from app.services.unit import (
    get_unit_parameter,
    add_unit_parameter,
)
from app.services.settings import get_period, get_parameter, get_unit


@units.route("/set_unit", methods=["GET", "POST"])
def set_unit():
    unit_id = request.args.get("unit_id")
    unit_category = request.args.get("unit_category")
    session["current_unit"] = unit_id
    session["current_unit_category"] = unit_category
    return redirect(url_for("units.unit_parameter", unit=unit_id))


@units.route("/<unit>/unit_parameter", methods=["GET", "POST"])
def unit_parameter(unit):
    return render_template("units/unit_parameter.html")


@units.route("/set_sec_unit", methods=["GET", "POST"])
def set_sec_unit():
    unit = request.args.get("data")
    session["current_sec_unit"] = unit
    return redirect(url_for("units.sec_unit_parameter", unit=unit))


@units.route("/<unit>/sec_unit_parameter", methods=["GET", "POST"])
def sec_unit_parameter(unit):
    return render_template("units/sec_unit_parameter.html")


@units.route("/set_planning_system", methods=["GET", "POST"])
def set_planning_system():
    unit = request.args.get("data")
    session["current_planning_system"] = unit
    return redirect(url_for("units.planning_system_parameter", unit=unit))


@units.route("/<unit>/planning_system", methods=["GET", "POST"])
def planning_system_parameter(unit):
    return render_template("units/planning_system_parameter.html")


# @units.route("/print", methods=["GET", "POST"])
# def print_parameters():
#     unit_parameters = prepare_unit_parameters(session["current_unit"])
#     unit = get_unit(session["current_unit"])
#     return render_template(
#         "units/print_daily.html", unit_parameters=unit_parameters, unit=unit
#     )


# @units.route("/unit_document/<year>", methods=["GET", "POST"])
# def unit_document(year=2024):
#     if request.method == "POST":
#         add_document(
#             session["current_unit"],
#             request.form["document_type_desc"],
#             request.form["period_desc"],
#             request.form["document_desc"],
#             request.form["creation_date"],
#             int(request.form["valid_year"]),
#             request.files["path"],
#         )
#         return redirect(url_for(".unit_document", year=2024))
#     else:
#         documents = get_documents(session["current_unit"], year)
#         document_types = get_document_types()
#         result = get_unit_documents(session["current_unit"])
#         print(documents)
#         return render_template(
#             "units/unit_document.html",
#             documents=documents,
#             result=result,
#             document_types=document_types,
#             current_year=year,
#         )


# @units.route("/control", methods=["GET", "POST"])
# def control():
#     if request.method == "POST":
#         add_unit_document(
#             session["current_unit"],
#             request.form["document_desc"],
#             request.form["period_desc"],
#         )
#         return redirect(url_for(".control"))
#     else:
#         document_types = get_document_types()
#         result = get_unit_documents(session["current_unit"])
#         return render_template(
#             "units/control.html",
#             document_types=document_types,
#             result=result,
#         )


# @units.route("/documents", methods=["GET", "POST"])
# def document():
#     if request.method == "POST":
#         # add_document(
#         #     session["current_unit"],
#         #     request.form["document_type_desc"],
#         #     request.form["period_desc"],
#         #     request.form["document_desc"],
#         #     request.form["creation_date"],
#         #     request.form["valid_Date"],
#         # )
#         file = request.files["file"]
#         return redirect(url_for(".control"))
#     else:
#         documents = get_documents(session["current_unit"])
#         document_types = get_document_types()
#         result = get_unit_documents(session["current_unit"])
#         return render_template(
#             "units/control.html",
#             documents=documents,
#             result=result,
#             document_types=document_types,
#         )


# @units.route("/show_status")
# def show():
#     return render_template("status.html")


# @units.route("/reports/<path:path>")
# def send_report(path):
#     return send_from_directory("all_documents", path)


@units.route("/upload_data", methods=["POST"])
def upload_data():
    data = request.json
    table_name = request.args["table_name"]
    if table_name == "unit_parameter":
        add_unit_parameter(data, session["current_unit"])
        return jsonify({})
    return jsonify({})


@units.route("/load_data", methods=["GET"])
def load_data():
    table_name = request.args["table_name"]
    if table_name == "unit_parameter":
        return jsonify(get_unit_parameter(session["current_unit"]))
    elif table_name == "period":
        return jsonify(get_period())
    elif table_name == "parameter":
        return jsonify(get_parameter(session["current_unit_category"]))
