from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    cgpa = data['cgpa']
    iq = data['iq']
    
    # Prepare input and make prediction
    input_data = [[cgpa, iq]]
    prediction = model.predict(input_data)
    
    # Return the result as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
