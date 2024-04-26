from models.base_model import db

# class Unit_Parameter(db.Model):
#     # unit_parameter_id = db.Column(db.Integer, primary_key=True)
#     unit_id = db.Column(db.Integer, db.ForeignKey("Unit.unit_id"), primary_key=True, nullable=False)
#     parameter_id = db.Column(db.Integer, db.ForeignKey("Parameter.parameter_id"), nullable=False)
#     period_id = db.Column(db.Integer, db.ForeignKey("Period.period_id"), nullable=False)
#     unit = db.relationship("Unit", back_populates='unit_parameter')
#     parameter = db.relationship("Parameter", back_populates='unit_parameter')
#     period = db.relationship("Period", back_populates='unit_parameter')