import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, precision_score
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib
from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

models = ["logistic", "multinb", "bernoullinb", "randomForest", "svm"]

variants = ["small", "medium", "large", "extreme"]

Models_file_map = {"logistic": "lr", "multinb": "MultinomialNB", "bernoullinb": "BernoulliNB", "randomForest": "rf", "svm": "svm"}


root_path = "./models"
base_filename = "spam_clf_model_"

def load_model(root_path, model, variant):
    base_filename = "spam_clf_model_"
    full_path = f'{root_path}/{base_filename}{model}_{variant}.pkl' 
    return joblib.load(full_path)

loaded_models = {
    model:{variant:load_model(root_path, Models_file_map[model], variant) 
           if os.path.isfile(f'{root_path}/{base_filename}{Models_file_map[model]}_{variant}.pkl')
           else None for variant in variants } 
    for model in models
    }
    
    
@app.route("/predict/<model>/<variant>/<email>")
def classifyEmail(model, variant, email):
    loaded_model = loaded_models[model][variant]
    if loaded_model is None:
        return {"prediction": f'Sorry, this model ({model} {variant}) is not available.'}
    
    pred = loaded_model.predict([email])[0]
    if pred == 0:
        return {"prediction": "Ham"}
    else:
        return {"prediction": "Spam"}





