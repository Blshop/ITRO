from models.base_model import db


class Deviation(db.Model):
    deviation_id = db.Column(db.Integer, primary_key=True)
    deviation_desc = db.Column(db.String(10), unique=True)
    parameters = db.relationship("Parameter", backref="deviation")


class Parameter(db.Model):
    parameter_id = db.Column(db.Integer, primary_key=True)
    parameter_desc = db.Column(db.String(20))
    fk_deviation = db.Column(
        db.Integer, db.ForeignKey("deviation.deviation_id"), nullable=False
    )
