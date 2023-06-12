import pickle
# import tensorflow as tf
import CONFIG

# model_rnn =tf.keras.models.load_model(r"saved_model/simpleRNN")

with open(CONFIG.ML_MODEL_PATH,"rb") as file:
    model = pickle.load(file) 
    
with open(CONFIG.VECTORIZER,"rb") as file: 
    vectorizer = pickle.load(file)
    
with open(CONFIG.TOKENIZER, "rb") as file: 
    tokenizer =  pickle.load(file)
    
with open(CONFIG.ENCODER,"rb") as file:
    encoder = pickle.load(file)



