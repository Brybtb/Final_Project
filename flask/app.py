from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib

sds = joblib.load("scaler.model")
clf = joblib.load("final_titanic_rf.model")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/predict')
def predict():
    
    
    age = request.args.get("age") or 0
    fare = request.args.get("fare") or 0
    sex = request.args.get("sex") or 0
    pclass3 = request.args.get("pclass3") or 0
    bin_sibsp = request.args.get("sibsp") or 0
    bin_parch = request.args.get("parch") or 0

    print("#"*80)
    features = [[sex, age, fare, pclass3, bin_sibsp, bin_parch]]
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
