import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

pc = PorterStemmer()


def transform_text(text):
    # lower case
    text = text.lower()
    # tokenize
    text = nltk.word_tokenize(text)
    # special characters removal
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    # stop words removal
    text = y[:]
    y = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # stemming
    text = y[:]
    y = []
    for i in text:
        y.append(pc.stem(i))
        # returning the list as a string
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model_mnb.pkl', 'rb'))

st.title("Spam Classifier")

input_sms = st.text_input("Enter the message: ")

if st.button('Predict'):
    #preprocess
    transformed_input = transform_text(input_sms)

    #vectorize
    vectorized = tfidf.transform([transformed_input])

    #predict
    result = model.predict(vectorized)[0]

    #display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')