from prediction import predict
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set title and description
st.title('Topic Identification for Health News Articles from 2015')
st.markdown('This is a Topic Modeling Natural Language Processing model that attempts to extract the topic of an article from the provided URL from CNN Health, NPR Health, CBC Health, LA Times Health and Everyday Health articles.')

# Input field for article URL
article_url = st.text_input(' Give Article URL below', '')

# Button to trigger topic classification
if st.button("Find Topic"):
    try:
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
    
    except RuntimeError as e:
        # Display error message
        st.error(str(e))


