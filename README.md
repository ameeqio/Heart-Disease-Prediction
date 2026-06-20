# 🫀 Heart Disease Prediction System

A machine learning-based web application that predicts the likelihood of heart disease based on patient health parameters.

## Overview

This project uses machine learning algorithms to analyze medical features and predict whether a patient is likely to have heart disease. Multiple classification models were evaluated, and the best-performing model was deployed using Streamlit.

## Features

* Data preprocessing and cleaning
* Feature engineering
* Model comparison and evaluation
* Interactive Streamlit web application
* Real-time heart disease prediction

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn
* SciPy

## Machine Learning Models Evaluated

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Naive Bayes
* Decision Tree

## Dataset Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

## Installation

```bash
git clone <repository-url>
cd heart-disease-prediction
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```text
heart-disease-prediction/
│
├── app.py
├── notebook.ipynb
├── heart_model.pkl
├── requirements.txt
└── README.md
```

## Results

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The best-performing model was selected and integrated into the Streamlit application.

## Future Improvements

* Hyperparameter tuning
* More advanced feature engineering
* Improved UI/UX
* Deployment to cloud platforms

## Author

Ameeq Akhtar
