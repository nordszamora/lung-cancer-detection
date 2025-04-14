import sys
import os
import pandas as pd

# Add the '/scripts' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from data.processing import process_original_dataset
from data.processing import process_synthetic_dataset
from data.processing import processing

# Test processing function for original set
def test_processing_original_dataset():
    for data in process_original_dataset().items():
        assert data

# Test processing function for synthetic set
def test_processing_synthetic_dataset():
    for data in process_synthetic_dataset().items():
        assert data

# Test execution function
def test_processing():
    process_original_dataset().to_csv('../data/processed/original.csv', index=False)
    process_synthetic_dataset().to_csv('../data/processed/synthetic.csv', index=False)

    assert 'Dataset Processed.'
