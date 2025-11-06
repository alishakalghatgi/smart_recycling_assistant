from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # allow requests from any origin

# ✅ Load your trained model here
model = joblib.load('waste_classifier.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    item = data.get('item')
    result = model.predict([item])[0]
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)