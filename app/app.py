
from prediction import predict
import streamlit as st

st.title('Classifying CNN Health News Articles from 2015')
st.markdown('This is a topic modelling Natural Language Processsing model that would try to extract the topic of article from the URL passed in the text underneath')

st.header("Give a news article link to know the topic it is related to")
article_url = st.text_input('Article URL', '')

if st.button("Find Topic"):
  result = predict(article_url)
  st.text("Topic seems to be most related to "+result)
