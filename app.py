from flask import Flask, request, render_template
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Khởi tạo Flask app
app = Flask(__name__)

# Load mô hình và tokenizer
model = tf.keras.models.load_model('BTL_model_dataphishingtank.keras')

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Tham số phải trùng với lúc huấn luyện
MAX_LEN = 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    seq = tokenizer.texts_to_sequences([url])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding='post', truncating='post')
    prob = model.predict(padded)[0][0]
    result = "Phishing" if prob > 0.5 else "Legitimate"
    return render_template('index.html', url=url, result=result, prob=round(prob * 100, 2))

if __name__ == '__main__':
    app.run(debug=True)
