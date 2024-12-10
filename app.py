from flask import (
    Flask,
    render_template,
    session,
)
from bp_settings.settings import settings_bp
from bp_units.units import units_bp
from bp_documents.documents import documents_bp
from bp_calendar.calendar import calendar_bp
from models.base_model import db
from functions.settings import get_units


app = Flask(__name__)

app.register_blueprint(settings_bp, url_prefix="/settings")
app.register_blueprint(units_bp, url_prefix="/units")
app.register_blueprint(documents_bp, url_prefix="/documents")
app.register_blueprint(calendar_bp, url_prefix="/calendar")
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:postgres@localhost:5432/ITRO"
)
app.add_url_rule(
    "/all_documents/<path:filename>",
    endpoint="all_documents",
    view_func=app.send_static_file,
)
db.init_app(app)


@app.route("/")
def index():
    session["units"] = [unit.unit_desc for unit in get_units()]
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True, host="127.0.0.1")
