from sklearn.linear_model import LogisticRegression, RidgeClassifier, PassiveAggressiveClassifier, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, IsolationForest, AdaBoostClassifier, StackingClassifier, GradientBoostingClassifier, HistGradientBoostingClassifier, VotingClassifier, BaggingClassifier
from sklearn.neighbors import RadiusNeighborsClassifier, KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import CategoricalNB, BernoulliNB, GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate

from time import time 
import warnings
import pandas as pd
import joblib
import os

warnings.filterwarnings('ignore')

# Load holdout training set
try:
    data = pd.read_csv(open(os.path.join(os.path.dirname(__file__), '../../data/input/train.csv'), 'r'))
except FileNotFoundError as err:
    print(f'Ann error occoured: {err}')

# Select every classifiers
def classifiers():
    estimators = {
        'logreg': LogisticRegression(solver='lbfgs', max_iter=200),
        'ridge': RidgeClassifier(),
        'passive_agressive': PassiveAggressiveClassifier(),
        'sgd': SGDClassifier(),
        'tree': DecisionTreeClassifier(),
        'extra_tree': ExtraTreesClassifier(),
        'random_forest': RandomForestClassifier(),
        'isolation_forest': IsolationForest(),
        'adaboost': AdaBoostClassifier(),
        'stacking': StackingClassifier(estimators=[('tree', DecisionTreeClassifier())]), 
        'gradient_boosting': GradientBoostingClassifier(), 
        'hist_gradient_boosting': HistGradientBoostingClassifier(), 
        'voting': VotingClassifier(estimators=[('tree', DecisionTreeClassifier())]), 
        'bagging': BaggingClassifier(),
        'radius_neighbors': RadiusNeighborsClassifier(), 
        'kneighbors': KNeighborsClassifier(),
        'svm': SVC(),
        'linear_svm': LinearSVC(),
        'categorical': CategoricalNB(),
        'bernoulli': BernoulliNB(), 
        'gaussian': GaussianNB(),
        'neural_net': MLPClassifier()
    }

    return estimators

# Train and perform validation to select the performing model
def train_validate(data):
    feature = data.drop('LUNG_CANCER', axis='columns')
    label = data['LUNG_CANCER']

    best_accuracy = 0
    best_precision = 0
    best_recall = 0
    best_f1 = 0
    best_model = None
    model_name = None

    for estimator_name, estimator in classifiers().items():
        cv = cross_validate(estimator, feature, label, scoring=['accuracy', 'precision', 'recall', 'f1'], cv=10)

        accuracy = cv['test_accuracy'].mean()
        precision = cv['test_precision'].mean()
        recall = cv['test_recall'].mean()
        f1 = cv['test_f1'].mean()
 
        if accuracy > best_accuracy:
           best_accuracy = accuracy
           best_precision = precision
           best_recall = recall
           best_f1 = f1
           model_name = estimator_name
           best_model = estimator

    return [model_name, best_accuracy, best_precision, best_recall, best_f1, best_model]

# Save the model 
def save_model(data):
    model_result = train_validate(data)

    print(f'\nBest Model: {model_result[0]}')
    print(f'Accuracy: {model_result[1]}')
    print(f'Precision: {model_result[2]}')
    print(f'Recall: {model_result[3]}')
    print(f'Measure: {model_result[4]}')
    
    model = model_result[5].fit(data.drop('LUNG_CANCER', axis='columns'), data['LUNG_CANCER'])

    model = joblib.dump(model, f'../../models/{model_result[0]}.joblib')
    return f'Model Saved: {model}'

if __name__ == '__main__':
   print(save_model(data))