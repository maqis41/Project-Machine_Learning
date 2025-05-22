from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apa')
def apa():
    return render_template('apa.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    data = request.form
    # Ambil data dari form predict.html
    age = data.get('age')
    sex = data.get('sex')
    cp = data.get('cp')
    # ... ambil semua field lain

    # Logika prediksi dummy (nanti diganti ML model)
    result = "Berisiko" if int(age) > 50 else "Tidak Berisiko"

    return f"<h1>Hasil Prediksi: {result}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
