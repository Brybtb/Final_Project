from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
import os
import numpy as np
import flask
from flask import Flask, render_template, request

sds = joblib.load("scaler.model2")
clf = joblib.load("RandomForestFinal.model1")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/api/predict')
def predict():
    
    # 'AvgGlucose', 'BMI', 'Age', 'EverMarried_Yes', 'ResidenceType_Urban', 'Gender_Male'
    AvgGlucose = request.args.get("AvgGlucose") or 0
    BMI = request.args.get("BMI") or 0
    Age = request.args.get("Age") or 0
    EverMarried_Yes = request.args.get("EverMarried_Yes") or 0
    ResidenceType_Urban = request.args.get('ResidenceType_Urban')
    Gender_Male = request.args.get("Gender_Male")

    #print("#"*80)
    features = [[AvgGlucose, BMI, Age, EverMarried_Yes, ResidenceType_Urban, Gender_Male]]
    print(features)

    scaled_features = sds.transform(features)
    print(scaled_features)

    spred = clf.predict(scaled_features)
    spred_prob = clf.predict_proba(scaled_features)

    print(spred)
    print(spred_prob)
    #print("#"*80)

    
    #return render_template('result.html', form=form)
    
@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result)==1:
            prediction='Income more than 50K'
        else:
            prediction='Income less that 50K'
        return render_template("result.html",prediction=prediction)

    return jsonify([{"survival_pred": spred.tolist(), 
                     "survival_probs": spred_prob.tolist(),
                     "features": features,
                     "scaled_features": scaled_features.tolist()}])




if __name__ == "__main__":
    app.run(debug=True)
