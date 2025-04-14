from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
import warnings
import pandas as pd
import joblib
import os

warnings.filterwarnings('ignore')

# Load trained model & holdout test set
try:
    model = joblib.load(open(os.path.join(os.path.dirname(__file__), '../../models/gradient_boosting.joblib'), 'rb'))
    data = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/input/test.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Predict holdout test set
def _predict(data):
    return model.predict(data.drop('LUNG_CANCER', axis='columns'))

# Get the score metrices
def score_metrics(data, metrics):
    return metrics(data['LUNG_CANCER'], _predict(data))

# Get the class matrix
def matrix(data, matrix):
    classes = matrix(data['LUNG_CANCER'], _predict(data))

    return f'TP: {classes[1][1]} - TN: {classes[0][0]} - FP: {classes[0][1]} - FN: {classes[1][0]}'

# Get the auc (TPR/FPR)
def auc(data):
    probs = model.predict_proba(data.drop('LUNG_CANCER', axis='columns'))[:, 1] 
    
    return roc_auc_score(data['LUNG_CANCER'], probs)

# Get the class reports
def report(data, class_metric):
    return class_metric(data['LUNG_CANCER'], _predict(data))

if __name__ == '__main__':
   print(f'Accuracy: {score_metrics(data, accuracy_score)}')
   print(f'Precision: {score_metrics(data, precision_score)}')
   print(f'Recall: {score_metrics(data, recall_score)}')
   print(f'Measure: {score_metrics(data, f1_score)}')
   print(f'\n{matrix(data, confusion_matrix)}')
   print(f'\nAUC: {auc(data)}')
   print(f'\n{report(data, classification_report)}')