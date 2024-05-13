from flask import (
    Flask,
    render_template,
    session,
)
from bp_settings.settings import settings_bp
from bp_units.units import units_bp
from models.base_model import db
from functions.settings import get_units


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
    session['units'] = [unit.unit_desc for unit in get_units()]
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")