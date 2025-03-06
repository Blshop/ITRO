import os
from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for,
    json,
    send_from_directory,
    current_app,
)
from . import calendar
from app.services.settings import (
    get_document_type,
    get_unit,
    get_period,
    get_organization,
)
from app.services.unit import add_document, get_document


@calendar.route("/calendar", methods={"GET", "POST"})
def load_calendar():
    document_types = get_document_type()
    units = get_unit("основные")
    periods = get_period()
    organizations = get_organization()
    return render_template(
        "calendar/calendar.html",
        document_types=document_types,
        units=units,
        periods=periods,
        organizations=organizations,
    )


# @calendar.route("/load_info/<year>", methods={"GET", "POST"})
# def load_info(year):
# documents = get_documents("Clinac iX", 2024)
# prepared_docs = prepare_docs_for_calendar(year)
# return json.dumps(prepared_docs)


@calendar.route("/load_documents/", methods={"GET"})
def load_documents():
    year = request.args["year"]
    units = request.args["unit"]
    document_types = request.args["document_type"]
    documents = get_document(units, document_types, year)
    return json.dumps(documents)


@calendar.route("/upload_document/", methods={"POST"})
def upload_documents():
    if request.method == "POST":
        add_document(
            request.form["unit_desc"],
            request.form["document_type_desc"],
            request.form["period_desc"],
            request.form["organization_desc"],
            request.form["document_desc"],
            request.form["start_date"],
            request.files["path"],
        )
    return redirect(url_for("calendar.load_calendar"))


@calendar.route("/load_document/<path:filename>", methods={"GET"})
def download_file(filename):
    full_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    absolute_path = os.path.abspath(full_path)
    directory = os.path.dirname(absolute_path)
    filename = os.path.basename(absolute_path)
    return send_from_directory(directory, filename)
