Diabetes Prediction Model

The library we have created contains a Machine Learning pipeline designed to predict the occurrence of diabetes mellitus using a dataset. The pipeline includes data loading, cleaning, model training, model evaluation and returns the predicted probabilities and the ROC_AUC score, evaluated on the test set. 
The model implemented has been a Random Forest Classifier. 

Requirements

To run this project, you will need the following libraries installed in your environment:

- Python >=3.8
- pandas (for data preprocessing and features creation)
- os (to build a platform-independent file path to ensure the CSV file is correctly     loaded from the same directory as the script) 
- scikit-learn (to implement the Random Forest Classifier model to split the data between train and test)
  - `sklearn.model_selection.train_test_split` (for splitting the data into train and test sets)
  - `sklearn.ensemble.RandomForestClassifier` (for training a Random Forest Classifier model)
  - `sklearn.metrics.roc_auc_score` (for computing ROC-AUC score)

Object-Oriented Design

The project follows the principles of Object-Oriented Programming. We have created multiple classes, each performing a specific task, which have been specified throughout the code. 

Classes are stored in Python files depending on the task their perform, so there are three different files: preprocessing.py, features_creation.py and prediction.py.


