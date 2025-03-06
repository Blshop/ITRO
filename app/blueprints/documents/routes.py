from flask import render_template, request
from . import documents
from app.services.settings import (
    get_unit,
    get_period,
)
from app.services.unit import print_unit_parameters

# from app.services.unit import print_unit_parameters


@documents.route("/protocols", methods={"GET", "POST"})
def protocols():
    periods = get_period()
    units = get_unit()
    return render_template(
        "documents/protocols.html",
        units=units,
        periods=periods,
    )


@documents.route("/print", methods=["GET", "POST"])
def print_parameters():

    data = request.json["data"]
    units = print_unit_parameters(data)
    date = [2025, "Февраль"]
    return render_template(
        "documents/print_daily.html", data=data, units=units, date=date
    )


# @documents_bp.route("/documents", methods={"GET", "POST"})
# def documents():
#     return render_template("documents/protocols.html")
