from flask import Flask, render_template, request , url_for
import pyqrcode

qr1 = Flask(__name__)

@qr1.route("/")
def index():
    return render_template("index.html")

@qr1.route('/generate_qr', methods=['POST'])  # Change the route to '/generate_qr'
def generate_qr():
    try:
        text = request.form['qr_data']
        qr_code = pyqrcode.create(text)
        qr_code.svg('static/qr_code.svg', scale=8)
        return render_template('index.html', qr_code='static/qr_code.svg')
    except Exception as e:
        print("Error generating QR code:", e)
        return "Error generating QR code"

if __name__ == '__main__':
    qr1.run(debug=True)
