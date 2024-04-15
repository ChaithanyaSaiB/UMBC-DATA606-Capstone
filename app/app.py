
"""from prediction import predict
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title('Classifying CNN Health News Articles from 2015')
st.markdown('This is a topic modelling Natural Language Processsing model that would try to extract the topic of article from the URL passed in the text underneath')

st.header("Give a news article link to know the topic it is related to")
article_url = st.text_input('Article URL', '')

if st.button("Find Topic"):
  result, article_words = predict(article_url)
  st.markdown("Topic seems to be most related to "+result)

  st.markdown("Word Cloud for the article is as follows")
  word_cloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(' '.join(article_words))

  fig = plt.figure(figsize = (8, 8), facecolor = None)
  plt.imshow(word_cloud)
  plt.axis("off")
  plt.tight_layout(pad = 0)

  st.pyplot(fig)"""

from prediction import predict
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set title and description
st.title('Classifying CNN Health News Articles from 2015')
st.markdown('This is a topic modeling Natural Language Processing model that attempts to extract the topic of an article from the provided URL.')

# Input field for article URL
article_url = st.text_input('Article URL', '')

# Button to trigger topic classification
if st.button("Find Topic"):
    # Display loading message
    with st.spinner('Analyzing article...'):
        # Call prediction function
        result, article_words = predict(article_url)
    
    # Display result
    st.success("Topic seems to be most related to: " + result)
    
    # Generate and display word cloud
    st.markdown("Word Cloud for the article:")
    word_cloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(' '.join(article_words))
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

