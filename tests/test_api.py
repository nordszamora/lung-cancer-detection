import pytest
import sys
import os

# Add the 'api' directory to sys.path so that Python can find the app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../api')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# Test api function
def test_model_prediction(client):
    data = {"gender": 1, "age": 43, "smoking": 2, "yellow_skin": 2, "fatigue": 2, "wheezing": 2, "coughing": 2, "shortness_of_breath": 2, "swallowing_difficulty": 2, "chest_pain": 2, "chronic_disease": 1}
    
    response = client.post('/api/v1/predict', json=data)
    assert response.json["prediction"] == 1