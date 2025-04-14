import sys
import os
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report

# Add the '/scripts' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from model.testing import _predict
from model.testing import score_metrics
from model.testing import matrix
from model.testing import auc
from model.testing import report

# Load holdout training set
try:
    data = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../data/input/test.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Test model prediction function
def test_prediction():
    assert _predict(data).any().astype(int)

# Test score metrics function
def test_metrics_score():
    assert score_metrics(data, accuracy_score)

# Test class matrix function
def test_class_matrix():
    assert matrix(data, confusion_matrix)

# Test auc function
def test_auc():
    assert auc(data)

# Test class report function
def test_class_report():
    assert report(data, classification_report)
