from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
from flask_cors import CORS
# import os
# import pandas as pd
# import numpy as np

scaler = joblib.load("scaler.model2")
randomforest = joblib.load("RandomForestFinal.model1")

app = Flask(__name__)
CORS(app)

# graphData = pd.read_csv("CleanedDataForModels.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')  
# def data():
#     graphData = graphData.to_dict(orient="record")
#     return jsonify(graphData)

@app.route('/api/predict')
def predict():
    
    AvgGlucose = request.args.get("AvgGlucose") or 0
    BMI = request.args.get("BMI") or 0
    Age = request.args.get("Age") or 0
    EverMarried_Yes = request.args.get("EverMarried_Yes") or 0
    ResidenceType_Urban = request.args.get('ResidenceType_Urban') or 0
    Gender_Male = request.args.get("Gender_Male") or 0
    features = [[AvgGlucose, BMI, Age, EverMarried_Yes, ResidenceType_Urban, Gender_Male]]
    print(features)

    scaled_features = scaler.transform(features)
    print(scaled_features)

    diagnosis_pred = randomforest.predict(scaled_features)
    diagnosis_pred_prob = randomforest.predict_proba(scaled_features)
    print(diagnosis_pred)
    print(diagnosis_pred_prob)
 
    if diagnosis_pred == 0:diagnosisText = 'Cardiovascular Disease is Not Present'
    else:diagnosisText = 'Cardiovascular Disease is Present'
    print(diagnosisText)

    return jsonify([{"diagnosisText": diagnosisText, 
                     "diagnisis_pred": diagnosis_pred.tolist(), 
                     "diagnosis_probs": diagnosis_pred_prob.tolist(),
                     "features": features,
                     "scaled_features": scaled_features.tolist()}])
   
if __name__ == "__main__":
    app.run(debug=True)
