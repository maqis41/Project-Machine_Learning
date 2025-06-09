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
    
    if prediction == 1:
        status = "Berisiko"
        paragraf1 = "Hasil prediksi menunjukkan bahwa Anda memiliki <strong>kemungkinan berisiko</strong> terhadap penyakit jantung. Meskipun ini <strong>bukan diagnosis pasti</strong>, hasil ini mencerminkan adanya <strong>faktor-faktor risiko</strong> yang perlu ditindaklanjuti dengan serius."
        paragraf2 = "saran yang bisa kami berikan: "
        tips = [
            "🥗 <strong>Perbaiki pola makan</strong> dengan mengurangi makanan tinggi lemak jenuh dan garam.",
            "🍎 <strong>Perbanyak konsumsi</strong> sayuran, buah-buahan, dan makanan tinggi serat.",
            "🚶‍♂️ <strong>Lakukan aktivitas fisik ringan</strong> secara rutin, seperti berjalan kaki minimal 30 menit sehari.",
            "🚭 <strong>Hindari merokok</strong> dan batasi konsumsi alkohol atau kafein.",
            "😴 <strong>Cukupi waktu istirahat</strong> dan hindari stres berlebihan.",
            "❗ Jika muncul gejala seperti <strong>nyeri dada</strong>, <strong>sesak napas</strong>, atau <strong>kelelahan ekstrem</strong>, segera cari bantuan medis."
        ]
        paragraf3 = "<strong>Konsultasi dengan dokter tetap sangat dianjurkan</strong> untuk evaluasi dan pemeriksaan lebih mendalam."
    else:
        status = "Tidak Berisiko"
        paragraf1 = "Hasil prediksi menunjukkan bahwa saat ini Anda <strong>tidak memiliki indikasi signifikan</strong> terhadap penyakit jantung. Ini menunjukkan kondisi kesehatan jantung Anda <strong>dalam batas normal</strong> berdasarkan data yang tersedia."
        paragraf2 = "saran yang bisa kami berikan: "
        tips = [
            "🍽️ <strong>Konsumsi makanan sehat</strong>, rendah lemak jenuh dan garam.",
            "🏃‍♀️ <strong>Tetap aktif secara fisik</strong>, seperti olahraga ringan hingga sedang secara rutin.",
            "🚭 <strong>Hindari rokok dan alkohol</strong> untuk menjaga fungsi jantung optimal.",
            "⚖️ <strong>Pertahankan berat badan ideal</strong> dan kendalikan gula darah serta tekanan darah.",
            "📅 <strong>Lakukan pemeriksaan kesehatan secara berkala</strong>, terutama jika memiliki riwayat keluarga dengan penyakit jantung."
        ]
        paragraf3 = "Hasil ini <strong>bukan jaminan bebas risiko di masa depan</strong>, jadi tetap jaga gaya hidup sehat dan rutin berkonsultasi dengan tenaga medis."

    return render_template(
        'predict.html', 
        prediction=True, 
        status=status, 
        paragraf1=paragraf1,
        paragraf2=paragraf2, 
        tips=tips,
        paragraf3=paragraf3
    )


if __name__ == '__main__':
    app.run(debug=True)