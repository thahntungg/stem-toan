from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sửa dòng này (phải có chữ er_template và ngoặc)
    return render_template('index.html')

@app.route('/bai-tap')
def baitap():
    return render_template('baitap.html')

if __name__ == '__main__':
    app.run(debug=True)
