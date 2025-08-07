from flask import Flask, request, jsonify
import joblib
import json
import numpy as np

# Load model and features
model = joblib.load('linear_mmm_model.pkl')

with open('mmm_model_features.json', 'r') as f:
    feature_names = json.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return "MMM Model is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract input features in order
    X = [data.get(feat, 0) for feat in feature_names]
    X = np.array(X).reshape(1, -1)
    
    prediction = model.predict(X)[0]
    return jsonify({'predicted_revenue': prediction})

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True, use_reloader=False)