# 🫀 Heart Disease Prediction System

A machine learning web application that predicts the likelihood of heart disease based on patient health parameters.

## 🚀 Live Demo

**Application:** https://heart-disease-prediction-gbfnynqyko8ftmgy9fjuzm.streamlit.app/

## 📌 Project Overview

This project uses machine learning classification algorithms to predict whether a patient is likely to have heart disease based on clinical and diagnostic features.

The project covers the complete machine learning workflow:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training
* Model Evaluation
* Model Deployment using Streamlit

## 📊 Dataset Features

The model uses the following patient attributes:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate Achieved
* Exercise-Induced Angina
* Oldpeak
* ST Slope

## 🤖 Models Evaluated

The following machine learning algorithms were compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Naive Bayes
* Decision Tree
* Random Forest Classifier
* XG Boost

The best-performing model was selected as Random Forest Classifier [accuracy : 88%, f1-score : 90%] and deployed in the application.

## 📈 Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

## 📂 Project Structure

heart-disease-prediction/

├── app.py

├── heart_model.pkl

├── exp_cols.pkl

├── notebook.ipynb

├── requirements.txt

└── README.md

## ⚙️ Installation

Clone the repository:

git clone <your-repository-url>

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## 🎯 Future Improvements

* Hyperparameter tuning
* Model explainability using SHAP
* Improved user interface
* Additional medical visualizations

## 👨‍💻 Author

Ameeq Akhtar

