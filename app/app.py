from prediction import predict
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set title and description
st.title('Topic Identification for Health News Articles from 2015')
st.markdown('This is a Topic Modeling Natural Language Processing model that attempts to extract the topic of an article from the provided URL from CNN Health, NPR Health, CBC Health, LA Times Health, and Everyday Health articles.')

# Sample links section
st.markdown('## Sample Links to Try:')
st.markdown('[1. Sabra Hummus Recalled in U.S. (CBC Health)](https://www.cbc.ca/news/health/sabra-hummus-recalled-in-u-s-1.3026865?cmp=rss)')
st.markdown('[2. COVID-19 Remains Deadlier than the Flu (LA Times Health)](https://www.latimes.com/science/story/2024-05-15/covid-19-remains-deadlier-than-the-flu)')
st.markdown('[3. Taylor Swift Joked that Jet Lag is a Choice (NPR Health)](https://www.npr.org/2024/05/16/1251278409/taylor-swift-joked-that-jet-lag-is-a-choice-a-sleep-expert-has-thoughts-about-th)')
st.markdown('[4. Alzheimer\'s Reversal (CNN Health)](https://www.cnn.com/2014/12/08/health/alzheimers-reversal/index.html?hpt=he_c1)')
st.markdown('[5. 10 Ways to Get Kids to Take Medicine (Everyday Health)](https://www.everydayhealth.com/kids-health/10-ways-to-get-kids-to-take-medicine.aspx)')

# Input field for article URL
article_url = st.text_input('Give Article URL below', '')

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
