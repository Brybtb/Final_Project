from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
from flask_cors import CORS

scaler = joblib.load("scaler.model2")
randomforest = joblib.load("RandomForestFinal.model1")

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')  

@app.route('/api/predict')
def predict():
    
    AvgGlucose1 = request.args.get("avgGlucose") or 0
    print('this is the avg glucose:' + str(AvgGlucose1))
    BMI = request.args.get("BMI") or 0
    Age = request.args.get("Age") or 0
    EverMarried_Yes = request.args.get("EverMarried_Yes") or 0
    ResidenceType_Urban = request.args.get('ResidenceType_Urban') or 0
    Gender_Male = request.args.get("Gender_Male") or 0
    features = [[AvgGlucose1, BMI, Age, EverMarried_Yes, ResidenceType_Urban, Gender_Male]]
    print(features)

    scaled_features = scaler.transform(features)
    print(scaled_features)

    diagnosis_pred = randomforest.predict(scaled_features)
    diagnosis_pred_prob = randomforest.predict_proba(scaled_features)
    probabilityDiseasePresent = randomforest.predict_proba(scaled_features)[:,1]
    print(diagnosis_pred)
    print(diagnosis_pred_prob)
    print(probabilityDiseasePresent)
    
    if any((diagnosis_pred_prob[0]) < 0.15):diagnosisText = 'Not At-Risk of Cardiovascular Disease'
    elif any((diagnosis_pred_prob[0]) < 0.225):diagnosisText = 'Slight Risk that Cardiovascular Disease is Present'
    elif any((diagnosis_pred_prob[0]) < 0.3):diagnosisText = 'Moderate Risk that Cardiovascular Disease is Present'
    else:diagnosisText = 'Significant Risk that Cardiovascular Disease is Present'
    print(diagnosisText)

    return jsonify([{
                     "features": features,
                     "scaled_features": scaled_features.tolist(),
                     "diagnisis_pred": diagnosis_pred.tolist(), 
                     "diagnosis_probs": diagnosis_pred_prob.tolist(),
                     "diagnosisText": diagnosisText, 
                     "probabilityDiseasePresent": probabilityDiseasePresent.tolist()
                     }])
   
if __name__ == "__main__":
    app.run(debug=True)
