'''
from app import db

class Data(db.Model):
   gender = db.Column(db.Integer, primary_key=True)
   age = db.Column(db.Integer, nullable=True)
   smoking = db.Column(db.Integer, nullable=True)
   yellow_skin = db.Column(db.Integer, nullable=True)
   fatigue = db.Column(db.Integer, nullable=True)
   wheezing = db.Column(db.Integer, nullable=True)
   coughing = db.Column(db.Integer, nullable=True)
   shortness_of_breath = db.Column(db.Integer, nullable=True)
   swallowing_difficulty = db.Column(db.Integer, nullable=True)
   chest_pain = db.Column(db.Integer, nullable=True)
   chronic_disease = db.Column(db.Integer, nullable=True)
   proba = db.Column(db.Float, nullable=True)
   label = db.Column(db.Integer, nullable=True)
'''