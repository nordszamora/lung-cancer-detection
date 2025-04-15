import joblib
import os

# Load trained model
try:
    GB_MODEL = os.path.join(os.path.dirname(__file__), '../../models/gradient_boosting.joblib')
    
    model = joblib.load(open(GB_MODEL, 'rb'))

except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')