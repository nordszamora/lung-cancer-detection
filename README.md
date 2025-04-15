# Lung Cancer Detection - v1.1

The machine learning project pipeline for lung cancer analysis and prediction at a low cost, to assist individuals in understanding their risk of lung cancer. It also supports decision making, health awareness, based on their lifestyle habits.

## Project Directory Structure

```
lung-cancer-detection/               # Root folder.
├── api/                               # Deploying model using flask for production.
├── data/                              # Different set of dataset.
|   ├── input/                           # Holdout set (training, testing).
|   ├── processed/                       # cleaned set (original, synthetic).
|   ├── raw/                             # un-processed set (original, synthetic).
├── figures/                           # Visualization charts.
|   ├── eda/                             # Exploratory analysis chart images.
|   |   ├── original/                      # Chart images for original part.
|   |   ├── synthetic/                     # Chart images for synthetic part.
|   ├── model/                           # Model evaluation chart images.
├── models/                            # Saved trained model.
├── notebooks/                         # Experimentation and analysis notebooks.
|   ├── data/                            # Notebooks for processing and preparations set.
|   ├── eda/                             # Exploratory analysis notebooks (original, synthetic).
|   ├── model/                           # Ml notebooks experimentation
|       ├── evaluation/                    # Notebook for training, validation and testing.
|       ├── inference/                     # Notebook for making prediction.
├── scripts/                           # Automated python scripts.
|   ├── data/                            # Scripts for processing and preparations set.
|   ├── model/                           # Scripts for model training, testing & inference.
├── tests/                             # Unit testing scripts (integration, functional).
├── .gitignore                         # Tells Git which files to ignore when committing your project.
├── LICENSE                            # Author license.
├── README.md                          # Project documentations for developers.
├── requirements.txt                   # Project installation dependencies.
```

## Model Pipeline Workflow

```
1. **Processing** - remove missing or duplicated data, feature engineering.
2. **Preparation** - feature selection, remove duplicated data, holdout split (train/test set).
3. **Training + cross val** - training + validation (training set), model selection.
4. **Testing** - model testing (test set).
5. **Inference** - make prediction for new data.
```

## Model Performance
  
  **Metrics**

  ```
  1. **Accuracy** - 93%
  2. **Precision** - 95%
  3. **Recall** - 91%
  4. **F1** - 93%
  ```

  **Matrix**

  ```
  TP: 43 - TN: 40 - FP: 2 - FN: 4
  ```

  **AUC**

  ```
  AUC - 0.97
  ```

  **Class Report**

  ```
  Class 0: Precision - 91%, Recall - 95%, F1 - 93% | Total - 42
  Class 1: Precision - 96%, Recall - 91%, F1 - 93% | Total - 47
  ```

The model used was gradient boosting (GB).

## Getting Started
Install this project on your local machine and here are following steps.

### Installation

   **Clone the Repository**

   ```
   $ git clone https://github.com/nordszamora/lung-cancer-detection.git

   $ cd lung-cancer-detection/

   $ pip install -r requirements.txt
   ```

### Automated Scripts
   1. **Run data scripts**

   ```
   $ cd scripts/

   $ cd data/

   $ python processing.py
   
   $ python preparation.py
   ```

   2. **Run model scripts**

   ```
   $ cd scripts/

   $ cd model/

   $ python training_validation.py
   
   $ python testing.py
   
   $ python inference.py
   ```

### Serving Model

   1. **Run flask api**

   ```
   $ cd api/

   $ python app.py
   ```

   2. **Test api endpoint**

   ```
   curl -X POST http://localhost:5000/api/v1/predict -H "Content-Type: application/json" -d '{"gender": 1, "age": 43, "smoking": 2, "yellow_skin": 2, "fatigue": 2, "wheezing": 2, "coughing": 2, "shortness_of_breath": 2, "swallowing_difficulty": 2, "chest_pain": 2, "chronic_disease": 1}'
   ```

### Unit Testing

   **Run pytest**

   ```
   $ cd tests/

   $ pytest
   ```

#### Data source:
See: ([kaggle](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer))

#### Note:
I used a SMOTE to generate a synthetic value due to poorly imbalance dataset.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
