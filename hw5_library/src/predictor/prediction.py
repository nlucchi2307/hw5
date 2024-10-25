from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

class DiabetesModel:
    def __init__(self, features, target):
        self.features = list(features)
        self.target = target
        self.model = RandomForestClassifier(random_state=42)
    
    def train(self, X_train, y_train):
        # train the model specified above on train set
        self.model.fit(X_train[self.features], y_train)
    
    def predict(self, X_test):
        # predict the target 
        return self.model.predict(X_test[self.features])
    
    def predict_proba(self, X_test):
        # get the probabilities to belong to class 1 (having diabetes)
        return self.model.predict_proba(X_test[self.features])[:, 1]  
    
    def evaluate(self, X_test, y_test):
        # evaluate the model with ROC-AUC metric
        y_pred_proba = self.predict_proba(X_test)
        return roc_auc_score(y_test, y_pred_proba)
