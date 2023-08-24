from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pipeline
pipeline = joblib.load('pipeline1.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        name = request.form['name']
        age = float(request.form['age'])
        gender = request.form['gender']
        location = request.form['location']
        subscription_length = float(request.form['subscription_length'])
        monthly_bill = float(request.form['monthly_bill'])
        total_usage = float(request.form['total_usage'])

        # Create a DataFrame with the input data
        #CustomerID	Name	Age	Gender	Location	Subscription_Length_Months	Monthly_Bill	Total_Usage_GB	Churn
        data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Location': [location],
            'Subscription_Length_Months': [subscription_length],
            'Monthly_Bill': [monthly_bill],
            'Total_Usage_GB': [total_usage], 
        })

        # Use the pipeline for preprocessing and prediction
        features = pipeline.named_steps['preprocessor'].transform(data)
        prediction = pipeline.named_steps['model'].predict(features)[0]

        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
