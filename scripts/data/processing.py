import warnings
import pandas as pd
import os

warnings.filterwarnings('ignore')

# Load the noisy dataset
try:
    original = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/raw/original.csv'), 'r'))
    synthetic = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/raw/synthetic.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Process the original set
def process_original_dataset():
    return original.drop_duplicates().dropna().replace({'M': 1, 'F': 2, 'YES': 1, 'NO': 0})
    
# Process the synthetic set
def process_synthetic_dataset():
    return synthetic.drop_duplicates().dropna().replace({'M': 1, 'F': 2, 'YES': 1, 'NO': 0})

# Processing results
def processing():
    process_original_dataset().to_csv('../../data/processed/original.csv', index=False)
    process_synthetic_dataset().to_csv('../../data/processed/synthetic.csv', index=False)

    return 'Dataset Processed.'

if __name__ == '__main__':
   print(processing())