from flask import Flask
from flask import jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer 

def tokens(string):
    """Break strings into characters."""
    return [x for x in string]
    
print("libraries imported")

df = pd.read_csv("/Users/tejes/Chrome-exten/PasswordManager/BackEnd/data.csv", on_bad_lines='skip')
df=df.dropna()
X=df.drop("strength",axis=1).values.flatten()
y=df["strength"].values
print("data processed")

with open('/Users/tejes/Chrome-exten/PasswordManager/BackEnd/password_model.pkl', 'rb') as file:
    model = pickle.load(file)

Checker = Flask(__name__)

@Checker.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@Checker.route('/model/', methods=['GET', 'POST'])
def display():
    try:
        return model.score(X,y)
    except Exception as e :
        return jsonify({"error": str(e)}),500

if __name__ == '__main__':
    Checker.run(host='0.0.0.0', port=105)

