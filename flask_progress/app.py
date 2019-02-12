from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
# import os
# import pandas as pd
# import numpy as np

sds = joblib.load("Scaler.model")
clf = joblib.load("RandomForestFinal.model")

app = Flask(__name__)

# graphData = pd.read_csv("CleanedDataForModels.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')  
def data():
    graphData = graphData.to_dict(orient="record")
    return jsonify(graphData)

@app.route('/api/predict')
def predict():
    
    # 'AvgGlucose', 'BMI', 'Age', 'EverMarried_Yes', 'ResidenceType_Urban', 'Gender_Male'
    avgGlucose = request.args.get("avgGlucose") or 0
    BMI = request.args.get("BMI") or 0
    age = request.args.get("age") or 0
    marriage = request.args.get("marriage") or 0
    gender = request.args.get("gender") or 0
    residence = request.args.get("residence") or 0

    print("#"*80)
    features = [[avgGlucose, BMI, age, gender, residence, marriage]]
    print(features)

    scaled_features = sds.transform(features)
    print(scaled_features)

    spred = clf.predict(scaled_features)
    spred_prob = clf.predict_proba(scaled_features)

    print(spred)
    print(spred_prob)
    print("#"*80)

    return jsonify([{"survival_pred": spred.tolist(), 
                     "survival_probs": spred_prob.tolist(),
                     "features": features,
                     "scaled_features": scaled_features.tolist()}])

if __name__ == "__main__":
    app.run(debug=True)
