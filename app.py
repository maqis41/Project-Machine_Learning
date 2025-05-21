from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
