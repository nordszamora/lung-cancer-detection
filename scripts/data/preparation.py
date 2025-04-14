from sklearn.model_selection import train_test_split
import warnings
import pandas as pd
import os

warnings.filterwarnings('ignore')

# Load processed datasets
try:
    original = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/processed/original.csv'), 'r'))
    synthetic = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/processed/synthetic.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# mix both original and synthetic sets
data = pd.concat([original, synthetic], keys=[1, 2]).drop_duplicates().dropna()

# Select relevant features
def feature_selection():
    feature = data[['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'FATIGUE', 'WHEEZING', 'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN', 'CHRONIC DISEASE']]
    label = data['LUNG_CANCER']
   
    return pd.concat([feature, label], axis=1).drop_duplicates().dropna()

# Split train/test holdout sets
def data_split(feature, label):
    X_train, X_test, y_train, y_test = train_test_split(feature, label, test_size=0.2, random_state=42, stratify=label)

    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test , y_test], axis=1)

    train_data.to_csv('../../data/input/train.csv', index=False)
    test_data.to_csv('../../data/input/test.csv', index=False)

    return f'Training set: {X_train.shape[0]} and Testing set: {X_test.shape[0]} save.'

if __name__ == '__main__':
   print(data_split(feature_selection().drop('LUNG_CANCER', axis='columns'), feature_selection()['LUNG_CANCER']))