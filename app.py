from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import os  # Import os to access environment variables

app = Flask(__name__, template_folder='templates')  # Set template folder
CORS(app)  # Enable CORS

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')  # Add this route
def home():
    return render_template('index.html')  # Load your HTML file

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    cgpa = data.get('cgpa')
    iq = data.get('iq')

    if cgpa is None or iq is None:
        return jsonify({'error': 'Missing input values'}), 400

    input_data = [[cgpa, iq]]
    prediction = model.predict(input_data)

    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use dynamic port for Render
    app.run(host='0.0.0.0', port=port)  # Bind to all IPs for deployment
