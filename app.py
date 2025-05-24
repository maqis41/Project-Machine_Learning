from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
    age = request.form.get('age')
    sex = request.form.get('sex')
    cp = request.form.get('cp')
    trestbps = request.form.get('trestbps')
    chol = request.form.get('chol')
    fbs = request.form.get('fbs')
    restecg = request.form.get('restecg')
    thalach = request.form.get('thalach')
    exang = request.form.get('exang')
    oldpeak = request.form.get('oldpeak')
    slope = request.form.get('slope')
    
    # Di sini nanti akan ditambahkan logika prediksi ML
    # Untuk sementara kita kembalikan hasil dummy
    prediction = "Berisiko" if int(age) > 50 else "Tidak Berisiko"
    
    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)