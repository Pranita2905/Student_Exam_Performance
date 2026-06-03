from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Simple, clean HTML UI embedded into the app for ease of deployment
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Predictor</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; margin: 40px; }
        .container { max-width: 500px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin: 0 auto; }
        h2 { text-align: center; color: #333; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; color: #666; }
        input[type="number"] { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .result { margin-top: 20px; padding: 15px; background-color: #e2f0d9; border-left: 5px solid #28a745; border-radius: 4px; font-size: 18px; text-align: center; }
    </style>
</head>
<body>

<div class="container">
    <h2>Performance Predictor</h2>
    <form method="POST" action="/predict">
        <div class="form-group">
            <label>Hours Studied:</label>
            <input type="number" name="hours_studied" step="0.1" required min="0">
        </div>
        <div class="form-group">
            <label>Previous Scores:</label>
            <input type="number" name="previous_scores" step="0.1" required min="0" max="100">
        </div>
        <div class="form-group">
            <label>Sleep Hours:</label>
            <input type="number" name="sleep_hours" step="0.1" required min="0" max="24">
        </div>
        <div class="form-group">
            <label>Sample Question Papers Practiced:</label>
            <input type="number" name="papers_practiced" required min="0">
        </div>
        <button type="submit">Predict Score</button>
    </form>

    {% if prediction is not none %}
    <div class="result">
        <strong>Predicted Score:</strong> {{ prediction }}
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE, prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs from form
        hours = float(request.form['hours_studied'])
        prev_scores = float(request.form['previous_scores'])
        sleep = float(request.form['sleep_hours'])
        papers = float(request.form['papers_practiced'])
        
        # Format the features for the model array shape: (1, 4)
        features = np.array([[hours, prev_scores, sleep, papers]])
        
        # Predict and bound the score logically between 0 and 100
        raw_prediction = model.predict(features)[0]
        final_prediction = max(0, min(100, round(raw_prediction, 2)))
        
        return render_template_string(HTML_TEMPLATE, prediction=final_prediction)
    
    except Exception as e:
        return f"An error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
