from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bai-tap')
def baitap():
    return render_template('baitap.html')

if __name__ == '__main__':
    app.run(debug=True)
