from flask import Blueprint, render_template, request, redirect, url_for, session, json

from functions.settings import get_periods
from functions.settings import get_units, get_unit, get_document_types
from functions.unit import (
    prepare_unit_parameters,
    print_period_parameters,
    get_documents,
    prepare_docs_for_calendar,
)


calendar_bp = Blueprint(
    "calendar_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@calendar_bp.route("/calendar", methods={"GET", "POST"})
def calendar():
    document_types = get_document_types()
    units = get_units()
    periods = get_periods()
    documents = get_documents("Clinac iX", 2024)
    prepared_docs = prepare_docs_for_calendar(2024)
    return render_template(
        "calendar/calendar.html",
        document_types=document_types,
        units=units,
        documents=documents,
        prepared_docs=json.dumps(prepared_docs),
        periods=periods,
    )


@calendar_bp.route("/load_info/<year>", methods={"GET", "POST"})
def load_info(year):
    # documents = get_documents("Clinac iX", 2024)
    prepared_docs = prepare_docs_for_calendar(year)
    return json.dumps(prepared_docs)
