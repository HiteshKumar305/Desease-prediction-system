from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cross-Origin requests allow karne ke liye, jo frontend alag origin se ho sakta hai
@app.route('/')
def home():
    return "Flask backend is running. Use /predict_stroke endpoint for prediction."

# Dummy prediction function
def predict_stroke(data):
    # Simple logic: agar age > 60 ya glucose > 140 toh stroke risk zyada maan ke "High Risk" return karo
    age = float(data.get('age', 0))
    glucose = float(data.get('glucose', 0))
    bmi = float(data.get('bmi', 0))
    hypertension = int(data.get('hypertension', 0))
    heartdisease = int(data.get('heartdisease', 0))
    # Dummy condition - tum yahan apni machine learning model ka logic use kar sakte ho
    if age > 60 or glucose > 140 or hypertension == 1 or heartdisease == 1 or bmi > 30:
        return "High Risk"
    else:
        return "Low Risk"

@app.route('/predict_stroke', methods=['POST'])
def predict_stroke_route():
    data = request.get_json(force=True)
    prediction = predict_stroke(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(port=5000)
