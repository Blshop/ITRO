from flask import Blueprint, render_template, request, redirect, url_for, session


units_bp = Blueprint(
    "units_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@units_bp.route("/units")
def general_data():
    return render_template("units/unit.html", menu_units=session["units"])


@units_bp.route("/<int:id>")
def unit_info(id=None):
    return render_template("units/unit.html", menu_units=session["units"])


@units_bp.route("/unit_calendar/<int:id>")
def unit_calendar(id=None):
    return render_template("units/calendar.html", menu_units=session["units"])


@units_bp.route("/unit_document/<int:id>")
def unit_document(id=None):
    return render_template("units/unit_document.html", menu_units=session["units"])
