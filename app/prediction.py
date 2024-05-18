# Importing necessary libraries
from webscraper import *
import re
import os
import io
import pandas as pd
import joblib
import streamlit as st
from gensim.corpora import Dictionary

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

index_to_topic = {
    0: "Healthcare Policy and Business",
    1: "Medical Research and Studies",
    2: "Entertainment and Sports",
    3: "Disease and Public Health",
    4: "Nutrition and Healthy Living"
}

@st.cache(allow_output_mutation=True)
def load_model_from_github(url):
    # Fetch the model content from the provided URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Read the model content as a bytes-like object
        content = io.BytesIO(response.content)
        
        # Load the model from the bytes-like object
        model = joblib.load(content)
        return model
    else:
        # Display an error message if the request failed
        st.error(f"Failed to load model from {url}. Status code: {response.status_code}")


# Function to clean text
def clean_text(text):
    # Remove HTML tags
    text = BeautifulSoup(text, 'html.parser').get_text()
    # Substitute hyphens with empty spaces
    text = re.sub(r'-', ' ', text)
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    return text

# Convert to wordnet tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None  # Use default POS for lemmatization
    
# Tokenize and preprocess text data
def preprocess_text(text):
    tokens = word_tokenize(text)  # Tokenize text
    lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
    pos_tags = nltk.pos_tag(tokens)  # Get part-of-speech tags
    for i, (token, tag) in enumerate(pos_tags):
        pos = get_wordnet_pos(tag)  # Convert NLTK POS tags to WordNet POS tags
        if pos:
            tokens[i] = lemmatizer.lemmatize(token, pos=pos)  # Lemmatize tokens
        else:
            tokens[i] = lemmatizer.lemmatize(token)  # Use default POS for lemmatization
    stop_words = set(stopwords.words('english'))  # Get stopwords
    custom_stopwords = [    # Custom stopwords
    "patient", "doctor", "say", "year", "state", "day", "need", "come", "well",
    "make", "think", "know", "go", "use", "one", "like", "people", "may",
    "many", "still", "even", "two", "way", "good", "much", "back", "new",
    "time", "first", "really",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    tokens = [token for token in tokens if token not in stop_words and token not in custom_stopwords]  # Remove stopwords
    return tokens

def predict(url):
    try:
        # Fetch and extract content from the URL
        raw_data = extract_body(fetch_content(url))
        if not raw_data:
            raise ValueError("Failed to extract content from the provided URL.")
        
        # Combine extracted paragraphs into a single string
        content = " ".join([p_tag.text.strip() for p_tag in raw_data])
        
        # Clean and preprocess the text data
        cleaned_data = clean_text(content)
        preprocessed_data = preprocess_text(cleaned_data)
        
        # Load the dictionary and LDA model
        model_dictionary = Dictionary.load('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/dictionary.sav')
        transformed_data = model_dictionary.doc2bow(preprocessed_data)

        lda_model = load_model_from_github('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/lda_model.sav')
        if not lda_model:
            raise ValueError("Failed to load the LDA model.")
        
        # Get the topic probabilities
        topics_probability = lda_model.get_document_topics(transformed_data)
        if not topics_probability:
            raise ValueError("Failed to compute topic probabilities.")
        
        # Determine the most likely topic
        topic_number = max(topics_probability, key=lambda x: x[1])[0]
        return index_to_topic.get(topic_number), preprocessed_data

    except Exception as e:
        # Raise a custom exception with the error message
        raise RuntimeError(f"Prediction failed: {str(e)}")

