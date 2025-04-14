import sys
import os
import pandas as pd

# Add the '/scripts' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from data.preparation import feature_selection
from data.preparation import data_split

# Test feature selection function
def test_feature_selection():
    for features in feature_selection().items():
        assert features

# Test data split function
def test_data_split():
    os.makedirs('../../data/input', exist_ok=True)

    assert data_split(feature_selection().drop('LUNG_CANCER', axis='columns'), feature_selection()['LUNG_CANCER'])
