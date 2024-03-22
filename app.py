from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    session,
)
from bp_settings.settings import settings_bp
from bp_units.units import units_bp
from models.base_model import db
from functions.settings import get_units
from acc_funct import get_unit, gather_info, menu

protocols = {}

app = Flask(__name__)

app.register_blueprint(settings_bp, url_prefix="/settings")
app.register_blueprint(units_bp, url_prefix="/units")
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:postgres@localhost:5432/ITRO"
)
db.init_app(app)


@app.route("/")
def index():
    units = get_units()
    session['units'] = [unit.unit_desc+' SN '+str(unit.unit_sn) for unit in units]
    print(session['units'])
    return render_template("index.html")


@app.route("/database/general_data")
def general_data():
    return render_template(
        "database/general_data/general_data.html", units=session["units"]
    )


@app.route("/equipment_type", methods={"GET", "POST"})
def equipment_types():
    if request.method == "POST":
        if request.form["equipment_type"] != "":
            equipment_type = request.form["equipment_type"]
            add_equipment_type(equipment_type)
        return redirect(url_for("equipment_types"))
    elif request.method == "GET":
        equipment_types = get_equipment_type()
        return render_template(
            "general_info/equipment_type.html",
            equipment_types=enumerate(equipment_types),
        )


@app.route("/selection")
def selection():
    return render_template("unit_selection.html")


@app.route("/add_unit")
def add_unit():
    return render_template("add_unit.html")


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/unit_parameter", methods=["GET", "POST"])
@app.route("/unit_parameter/<int:id>", methods=["GET", "POST"])
def unit_parameter(id=None):
    if request.method == "POST":
        set_quality_control(
            request.form["parameter_desc"], request.form["period_desc"], id
        )
        return redirect(url_for("unit_parameter", id=id))
    elif request.method == "GET":
        units = get_units()
        parameters = get_parameters()
        periods = get_period()
        unit_parameters = get_quality_control(id)
        active_unit = get_unit(id)
        return render_template(
            "quality_control/unit_parameter.html",
            units=units,
            parameters=parameters,
            periods=periods,
            unit_parameters=unit_parameters,
            unit=active_unit,
        )


@app.route("/control_protocol")
def control_protocol():
    periods = [x.period_desc for x in get_period()]
    protocols = get_protocols()
    units = [x.id for x in get_units()]
    return render_template(
        "quality_control/select_protocol.html",
        periods=periods,
        protocols=protocols,
        units=units,
    )


@app.route("/daily", methods=["GET", "POST"])
def daily():
    if request.method == "POST":
        data = request.get_json()
        global protocols
        protocols = gather_info(data)
        return jsonify(dict(redirect="/daily"))
    else:
        data = protocols
        print(data)
        return render_template(
            "quality_control/protocol/protocol.html", data=data, width=11
        )


@app.route("/units/document", methods={"GET", "POST"})
# @app.route("/database/general_data/deviation/<int:id>", methods={"POST"})
def document():
    if request.method == "POST":
        if request.form["submit_button"] == "Исправить":
            edit_deviation(request.form["deviation_value"], id)
        else:
            add_deviation(request.form["deviation_value"])
        return redirect(url_for("deviation"))
    elif request.method == "GET":
        deviations = get_deviation()
        return render_template("units/document.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
