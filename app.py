
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Đây là đoạn để sửa lỗi 404 cho trang bài tập
@app.route('/bai-tap')
def baitap():
    return render_template('baitap.html')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# Trang chủ - Lý thuyết (400 dòng của bạn)
@app.route('/')
def home():
    return render_template('index.html')

# Trang bài tập - Trắc nghiệm & Tự luận (500 dòng của bạn)
@app.route('/bai-tap')
def baitap():
    return render_template('bai-tap.html')

if __name__ == '__main__':
    # Render sẽ cung cấp cổng PORT tự động thông qua biến môi trường
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
