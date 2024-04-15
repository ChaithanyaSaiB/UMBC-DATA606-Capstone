
from prediction import predict
import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title('Classifying CNN Health News Articles from 2015')
st.markdown('This is a topic modelling Natural Language Processsing model that would try to extract the topic of article from the URL passed in the text underneath')

st.header("Give a news article link to know the topic it is related to")
article_url = st.text_input('Article URL', '')

if st.button("Find Topic"):
  result, article_words = predict(article_url)
  st.text("Topic seems to be most related to "+result)

  word_cloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                #stopwords = set(STOPWORDS),
                min_font_size = 10).generate(article_words.str.cat(sep = ' '))

# plot the WordCloud image
fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(word_cloud)
plt.axis("off")
plt.tight_layout(pad = 0)

st.pyplot(fig)
