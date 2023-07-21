import streamlit as st
import numpy as np
import config
import model


test_model = model.Model()


st.title("Movie Review Classification Page:cinema:")
#st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
st.text("""This is a movie review classification web page which predicts whether 
the review is positive or negative using NLP algorithm.
This model is still under devlopment and not the final product.
It may give wrong prediction so use it for test purpose only :)""")



text = st.text_area("Type movie review","This is good movie")

def result():
    if text:

        pred = test_model.result(text)

        if pred== 0:
            return st.error("This is negative review:thumbsdown:")
        else:
            return st.success("This is posititve review:thumbsup:")
    else:
        return st.error("No text entered")

st.button("Predict",on_click=result)

