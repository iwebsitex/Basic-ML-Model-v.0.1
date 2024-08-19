from flask import Flask, render_template, request
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('model.joblib')  # Assuming 'model.joblib' is in the same directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        cgpa = float(request.form['cgpa'])

        # Prepare the data
        data = pd.DataFrame([[cgpa]], columns=['cgpa'])

        # Make prediction using the loaded model
        prediction = model.predict(data)[0]

        return render_template('index.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Or any other available port

