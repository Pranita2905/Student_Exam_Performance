
# Student Performance Prediction
## Live 
[Student Performance Prediction App](https://u3dsi3ppaafd6pnocddcwq.streamlit.app)
## Overview

This project predicts a student's Performance Index using Machine Learning based on:

* Hours Studied
* Previous Scores
* Sleep Hours
* Sample Question Papers Practiced

The model is trained using Multiple Linear Regression from Scikit-Learn and deployed using Streamlit.

---

## Dataset

Dataset: Student Performance Dataset

Features:

* Hours Studied
* Previous Scores
* Sleep Hours
* Sample Question Papers Practiced

Target Variable:

* Performance Index

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Pickle
* Streamlit

---

## Machine Learning Workflow

### 1. Data Collection

Collected the Student Performance dataset.

### 2. Data Preprocessing

* Removed unnecessary columns.
* Selected relevant features.
* Checked for missing values.

### 3. Feature Selection

Input Features:

* Hours Studied
* Previous Scores
* Sleep Hours
* Sample Question Papers Practiced

Output:

* Performance Index

### 4. Model Training

Algorithm Used:

* Multiple Linear Regression

Data Split:

* Training Data: 80%
* Testing Data: 20%

### 5. Model Evaluation

Evaluation Metric:

* R² Score

The model was trained and saved as:

model.pkl

---

## Project Structure

```bash
Student_Performance_Project/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── Student_Performance.csv
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Student_Performance_Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

For Streamlit:

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

---

## Sample Input

| Feature                 | Value |
| ----------------------- | ----- |
| Hours Studied           | 8     |
| Previous Scores         | 85    |
| Sleep Hours             | 7     |
| Sample Papers Practiced | 10    |

---

## Sample Output

```text
Predicted Performance Index: 87.45
```

---

## Future Improvements

* Hyperparameter Tuning
* Feature Engineering
* Advanced Regression Models
* Model Deployment on Cloud
* Interactive Dashboard

---

## Author

Pranita Mothe
Data Analyst | Machine Learning Enthusiast
