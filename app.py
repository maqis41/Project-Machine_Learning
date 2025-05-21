from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/apa')
def apa():
    return send_from_directory('.', 'apa.html')

@app.route('/kontak')
def kontak():
    return send_from_directory('.', 'kontak.html')

@app.route('/predict')
def predict():
    return send_from_directory('.', 'predict.html')

# Optional: agar bisa akses file gambar dan js
@app.route('/img/<path:filename>')
def serve_images(filename):
    return send_from_directory('img', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

if __name__ == '__main__':
    app.run(debug=True)
