from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model_path = 'model/model_file.p'
with open(model_path, 'rb') as file:
    model = pickle.load(file)['model']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs from form
        input_features = [float(x) for x in request.form.values()]
        final_features = np.array(input_features).reshape(1, -1)
        prediction = model.predict(final_features)[0]

        return render_template('home.html', prediction_text=f'Predicted Runs: {round(prediction, 2)}')
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
