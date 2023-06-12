from flask import Flask, request, render_template
from load_objects import model
from utils import clean_text
import numpy as np 
from keras.utils import pad_sequences
import CONFIG


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods = ["POST"])
def predict_ml():

    input_news = request.form

    clean_news = clean_text(input_news["news"])
    news_vector = vectorizer.transform([clean_news])
    result = model.predict(news_vector)[0]
    print(f"Prediction from Model = {result}")
  
    # clean_news = clean_text(input_news["news"])
    # text_seq = tokenizer.texts_to_sequences(clean_news)
    # text_padpad_sequences= pad_sequences(text_seq, maxlen=130)
    # result_predict = model_rnn.predict(text_padpad_sequences)
    # prediction = encoder.inverse_transform([np.argmax(result_predict[0])])[0]
    # print(f"Prediction from DL = {prediction}")
    prediction = "GPU NOT AVIALABLE"

    return render_template("index.html", ML_RESULT = result, DL_RESULT=prediction )

if __name__=="__main__":
    app.run(host=CONFIG.HOST,port=CONFIG.PORT, debug=True)