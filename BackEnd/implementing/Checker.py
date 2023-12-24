from flask import Flask
from flask import request, jsonify
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
    
# print("libraries imported")

# df = pd.read_csv("/Users/tejes/Chrome-exten/PasswordManager/BackEnd/data.csv", on_bad_lines='skip')
# df=df.dropna()
# X=df.drop("strength",axis=1).values.flatten()
# y=df["strength"].values
# print("data processed")

with open('C:\PasswordManager\BackEnd\password_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_password_strength(user_password):
    predicted_strength = model.predict([user_password])
    return predicted_strength

Checker = Flask('PasswordChecker')

@Checker.route('/predict', methods=['GET', 'POST'])
def display():
    try:
        data = request.get_json()
        # Extract the user's password from the JSON data
        # Get the JSON data from the request
        if 'user_password' not in data:
            return jsonify({'error': 'Invalid JSON structure'}), 400
        
        user_password = data['user_password']
        # Call the prediction function
        password_strength = predict_password_strength(user_password)

        return jsonify({'password_strength': int(password_strength)})
    
    except Exception as e :
        return jsonify({"error": str(e)}),500

if __name__ == '__main__':
    Checker.run(debug = True, host='0.0.0.0', port=105)

