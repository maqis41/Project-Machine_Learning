import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Muat model dan scaler yang sudah disimpan
model = joblib.load('svm_heart_disease_model.joblib')  # Sesuaikan path/nama file
scaler = joblib.load('scaler.joblib')  # Sesuaikan path/nama file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apa.html')
def apa():
    return render_template('apa.html')

@app.route('/kontak.html')
def kontak():
    return render_template('kontak.html')

@app.route('/predict.html')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form
    age = float(request.form.get('age'))
    sex = 0 if request.form.get('sex') == 'M' else 1  # Sesuaikan mapping
    cp = float(request.form.get('cp'))  # ChestPainType: ATA=0, NAP=1, ASY=2, TA=3
    trestbps = float(request.form.get('trestbps'))
    chol = float(request.form.get('chol'))
    fbs = float(request.form.get('fbs'))
    thalach = float(request.form.get('thalach'))
    exang = 0 if request.form.get('exang') == 'N' else 1  # ExerciseAngina: N=0, Y=1

    # Pastikan urutan fitur sama dengan saat training
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, thalach, exang]])
    
    # Preprocess: normalisasi dengan scaler
    input_scaled = scaler.transform(input_data)
    
    # Prediksi dengan model
    prediction = model.predict(input_scaled)[0]
    result = "Berisiko (Heart Disease)" if prediction == 1 else "Tidak Berisiko (No Heart Disease)"
    
    return render_template('predict.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)