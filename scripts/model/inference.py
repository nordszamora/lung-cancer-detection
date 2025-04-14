from time import time 
import warnings
import joblib
import sys
import os

warnings.filterwarnings('ignore')

# Load trained model
try:
    model = joblib.load(open(os.path.join(os.path.dirname(__file__), '../../models/gradient_boosting.joblib'), 'rb'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Predict new data
def predict(data):
    return model.predict([data])[0]

# Get the prediction outcome
def proba(data):
    return f'{(model.predict_proba([data])[0][predict(data)] * 100):.0f}%'

# Result
def main(data):
    timer = time()

    prediction = predict(data)

    if prediction == 1:
       return f'Prediction: {proba(data)} - Affected | Prediction speed: {(time() - timer):.3f}'
    else:
       return f'Prediction: {proba(data)} - Benign | Prediction speed: {(time() - timer):.3f}'

if __name__ == '__main__':
   print(main([1,24,1,1,2,1,1,2,1,1,1])) # My health status