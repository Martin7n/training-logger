from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)
    sent_to_flask = db.Column(db.Boolean, default=False, nullable=False)
    sent_at = db.Column(db.DateTime(timezone=True),nullable=True)
    data = db.Column(db.JSON, nullable=False)