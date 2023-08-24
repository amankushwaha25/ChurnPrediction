# Churn Prediction Project Documentation

Welcome to the Churn Prediction project documentation. This documentation provides an overview of the project's purpose, features, installation instructions, usage guide, and more.

## Installation

To run this project, you need the following dependencies:

Python

```bash
pip install -r requirements.txt
```

## Usage

1. Run flask application
```bash 
python app.py
```
2. Open a web browser and go to http://localhost:5000.
3. Fill out the form with customer details and click "Predict" to receive the churn prediction.

## Data Preprocessing

1. The data preprocessing pipeline handles missing values and encodes categorical features.
2. Missing values are imputed using the mean for numerical attributes and the mode for categorical attributes.

## Model Training

The machine learning model is a Random Forest Classifier, trained to predict customer churn based on historical data.

## Web Interface

The web interface provides an interactive way to input customer data and get churn predictions.
Users can fill out a form on the website to obtain predictions.

## Sample Input and Output
Input:

Customer ID: C12345\
Name: John Doe\
Age: 30\
Gender: Male\
Location: Houston\
Subscription Length (Months): 12\
Monthly Bill: 50.00\
Total Usage (GB): 100.0\
Output:
Churn Prediction: Not Churn (0)

## Future Plans

Improve user interface with enhanced visualizations.
Explore more advanced machine learning algorithms for prediction accuracy improvement.

## Contact Information
For questions or feedback, contact Aman Kushwaha \
Email id: kushwahaaman2505@gmail.com
