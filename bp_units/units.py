from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    send_from_directory,
)
from functions.settings import get_parameters, get_periods, get_unit, get_document_types
from functions.unit import (
    add_unit_parameter,
    prepare_unit_parameters,
    prepare_rest_unit_parameters,
    add_unit_document,
    get_unit_documents,
    get_all_unit_document_types,
    add_document,
    get_documents,
)
import os


units_bp = Blueprint(
    "units_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@units_bp.route("/<current_unit>", methods=["GET", "POST"])
def unit(current_unit):
    session["current_unit"] = current_unit
    return render_template("unit.html")


@units_bp.route("/unit_parameter", methods=["GET", "POST"])
def unit_parameter():
    if request.method == "POST":
        add_unit_parameter(
            session["current_unit"],
            request.form["parameter_desc"],
            request.form["period_desc"],
        )
        return redirect(url_for(".unit_parameter"))
    else:
        parameters = prepare_rest_unit_parameters(session["current_unit"])
        periods = get_periods()
        result = prepare_unit_parameters(session["current_unit"])
        return render_template(
            "units/unit_parameter.html",
            parameters=parameters,
            periods=periods,
            result=result,
        )


@units_bp.route("/print", methods=["GET", "POST"])
def print_parameters():
    unit_parameters = prepare_unit_parameters(session["current_unit"])
    unit = get_unit(session["current_unit"])
    return render_template(
        "units/print_daily.html", unit_parameters=unit_parameters, unit=unit
    )


@units_bp.route("/unit_document/<path>", methods=["GET", "POST"])
def unit_document(path=None):
    if request.method == "POST":
        add_document(
            session["current_unit"],
            request.form["document_type_desc"],
            request.form["period_desc"],
            request.form["document_desc"],
            request.form["creation_date"],
            int(request.form["valid_year"]),
            request.files["path"],
        )
        return redirect(url_for(".control"))
    else:
        documents = get_documents(session["current_unit"])
        document_types = get_document_types()
        periods = get_periods()
        result = get_unit_documents(session["current_unit"])
        print(documents)
        return render_template(
            "units/unit_document.html",
            documents=documents,
            periods=periods,
            result=result,
            document_types=document_types,
            path="2024/casio.pdf",
        )


@units_bp.route("/control", methods=["GET", "POST"])
def control():
    if request.method == "POST":
        add_unit_document(
            session["current_unit"],
            request.form["document_desc"],
            request.form["period_desc"],
        )
        return redirect(url_for(".control"))
    else:
        document_types = get_document_types()
        periods = get_periods()
        result = get_unit_documents(session["current_unit"])
        return render_template(
            "units/control.html",
            document_types=document_types,
            periods=periods,
            result=result,
        )


@units_bp.route("/documents", methods=["GET", "POST"])
def document():
    if request.method == "POST":
        # add_document(
        #     session["current_unit"],
        #     request.form["document_type_desc"],
        #     request.form["period_desc"],
        #     request.form["document_desc"],
        #     request.form["creation_date"],
        #     request.form["valid_Date"],
        # )
        file = request.files["file"]
        return redirect(url_for(".control"))
    else:
        documents = get_documents(session["current_unit"])
        document_types = get_document_types()
        periods = get_periods()
        result = get_unit_documents(session["current_unit"])
        return render_template(
            "units/control.html",
            documents=documents,
            periods=periods,
            result=result,
            document_types=document_types,
        )


@units_bp.route("/show_status")
def show():
    return render_template("status.html")


@units_bp.route("/reports/<path:path>")
def send_report(path):
    return send_from_directory("all_documents", path)
