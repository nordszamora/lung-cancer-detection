import sys
import os

# Add the '/scripts' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from model.inference import main

# Test model prediction function
def test_inference():
    assert main([1,24,1,1,2,1,1,2,1,1,1])