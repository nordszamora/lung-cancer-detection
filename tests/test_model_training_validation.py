import sys
import os
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Add the '/scripts' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from model.training_validation import classifiers
from model.training_validation import train_validate
from model.training_validation import save_model

# Load holdout training set
try:
    data = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../data/input/train.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Test the classifier collections
def test_classifier_selection():
    assert classifiers()

# Test the training + validation function
def test_train_validate():
    assert train_validate(data)

# Test model saving function
def test_saving_model():
    os.makedirs('../../models', exist_ok=True)
    
    assert save_model(data)
