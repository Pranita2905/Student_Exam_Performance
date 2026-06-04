from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load Model
model = pickle.load(open("model.pkl", "rb"))

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Performance Predictor</title>
    <style>
        body{
            font-family: Arial;
            background-color:#f4f4f4;
            text-align:center;
            padding-top:50px;
        }
        .container{
            width:400px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        }
        input{
            width:90%;
            padding:10px;
            margin:8px;
        }
        button{
            background:#007bff;
            color:white;
            padding:10px 20px;
            border:none;
            border-radius:5px;
            cursor:pointer;
        }
        h3{
            color:green;
        }
    </style>
</head>
<body>

<div class="container">

<h2>Student Performance Prediction</h2>

<form method="POST">

<input type="number" step="any" name="hours_studied" placeholder="Hours Studied" required><br>

<input type="number" step="any" name="previous_scores" placeholder="Previous Scores" required><br>

<input type="number" step="any" name="sleep_hours" placeholder="Sleep Hours" required><br>

<input type="number" step="any" name="sample_papers" placeholder="Sample Papers Practiced" required><br>

<button type="submit">Predict</button>

</form>

{% if prediction %}
<h3>{{ prediction }}</h3>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        features = np.array([[
            float(request.form["hours_studied"]),
            float(request.form["previous_scores"]),
            float(request.form["sleep_hours"]),
            float(request.form["sample_papers"])
        ]])

        result = model.predict(features)[0]

        prediction = f"Predicted Performance Index: {result:.2f}"

    return render_template_string(html, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
