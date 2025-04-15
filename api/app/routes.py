from flask import Blueprint, request, jsonify
import joblib
import os

from app.load_model import model

blueprint = Blueprint('blue_print', __name__)

# Prediction request
@blueprint.route('/predict', methods=['POST'])
def predict():
    # Get the new value
    gender = request.json.get('gender')
    age = request.json.get('age')
    smoking = request.json.get('smoking')
    yellow_skin = request.json.get('yellow_skin')
    fatigue = request.json.get('fatigue')
    wheezing = request.json.get('wheezing')
    coughing = request.json.get('coughing')
    shortness_of_breath = request.json.get('shortness_of_breath')
    swallowing_difficulty = request.json.get('swallowing_difficulty')
    chest_pain = request.json.get('chest_pain')
    chronic_disease = request.json.get('chronic_disease')

    # Value type request
    def convert_data(data):
        if isinstance(data, int):
           return int(data)
        
        elif isinstance(data, str):
           return str(data)

    # Input data for prediction
    data = [
            convert_data(gender), 
            convert_data(age), 
            convert_data(smoking), 
            convert_data(yellow_skin), 
            convert_data(fatigue), 
            convert_data(wheezing), 
            convert_data(coughing), 
            convert_data(shortness_of_breath), 
            convert_data(swallowing_difficulty), 
            convert_data(chest_pain), 
            convert_data(chronic_disease)
           ]

    pred = model.predict([data])[0] # Predict new data
    proba = model.predict_proba([data])[0][pred] # Get the prediction outcome

    return jsonify({'prediction': int(pred), 'proba': float(proba)}), 200
