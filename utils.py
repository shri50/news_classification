""" fuction for the api"""
import re
from wordcloud import STOPWORDS

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]',' ', text)
    text = text.strip()
    
    # remove stop words
    text = [word for word in text.split() if word not in list(STOPWORDS)]
    
    text = " ".join(text)
    return text