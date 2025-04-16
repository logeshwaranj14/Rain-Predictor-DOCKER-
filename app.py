from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data.get(f) for f in ["MinTemp", "MaxTemp", "Rainfall", "Humidity9am", "Humidity3pm"]]
    
    if None in features:
        return jsonify({"error": "Missing feature values"}), 400
    
    prediction = model.predict([features])[0]
    return jsonify({"prediction": int(prediction), "rain": "Yes" if prediction == 1 else "No"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
