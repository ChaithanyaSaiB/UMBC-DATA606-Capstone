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



'''
def fetch_content(url):
    """
    Fetches the content of a webpage from the given URL.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The content of the webpage as a string, or None if fetching fails.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print("Error fetching content:", e)
        return None

def extract_body(html_content):
    """
    Extracts the body content from HTML using BeautifulSoup.

    Args:
        html_content (str): The HTML content of a webpage.

    Returns:
        list: A list of paragraph tags containing the body content, or None if extraction fails.
    """
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        article_body = soup.findAll('p', class_='paragraph')
        if article_body:
            return article_body
        else:
            return None
    else:
        return None

def split_string_with_special_characters(word_list):
    """
    Splits strings in a list based on special characters.

    Args:
        word_list (list): A list of words.

    Returns:
        list: A list of words split based on special characters.
    """
    pattern = r'[-\s]'
    for word in word_list:
        if re.search(r'[-\s]', word):
            substrings = re.split(pattern, word)
            substrings = [substr for substr in substrings if substr]
            word_list.remove(word)
            word_list.extend(substrings)
    return word_list

def lowercase_words_and_lemmatize(word_list):
    """
    Converts words to lowercase and lemmatizes them.

    Args:
        word_list (list): A list of words.

    Returns:
        list: A list of lemmatized words.
    """
    word_list_lower = [word.lower() for word in word_list]
    pos_tags = nltk.pos_tag(word_list_lower)

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
            return wordnet.NOUN

    lemmatized_words = []
    lemmatizer = WordNetLemmatizer()
    for word, tag in pos_tags:
        pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos=pos)
        lemmatized_words.append(lemma)

    return lemmatized_words

def stopwords_removal(word_list):
    """
    Removes stopwords from a list of words.

    Args:
        word_list (list): A list of words.

    Returns:
        list: A list of words with stopwords removed.
    """

    # Define parts of speech to remove
    parts_of_speech_to_remove = ['NN', 'VB', 'JJ']
    
    tagged_words = nltk.pos_tag(word_list)
    stop_words = set(stopwords.words('english'))

    github_url = "https://github.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/blob/main/app/custom%20stopwords.txt"
    custom_stopwords = read_text_from_github(github_url).split()
  
    return [word for word, pos in tagged_words if pos not in parts_of_speech_to_remove 
            and word not in stop_words and word not in custom_stopwords]

def remove_non_alphabetic_and_custom_stopwords(word_list):
    """
    Removes non-alphabetic characters and custom stopwords from a list of words.

    Args:
        word_list (list): A list of words.

    Returns:
        list: A list of words with non-alphabetic characters and custom stopwords removed.
    """
    english_words = set(nltk.corpus.words.words())
    return [word for word in [re.sub(r'[^a-zA-Z]', '', word) for word in word_list] if word in english_words]

index_to_topic = {
    0: "Vaccination and Measles",
    1: "Medical Treatments and Marijuana",
    2: "Health Research and Findings",
    3: "Childhood Mental Health and Education",
    4: "Infectious Diseases and Hygiene",
    5: "Food and Nutrition",
    6: "Family Health and Illness",
    7: "Personal Health and Weight Management",
    8: "Healthcare System and Cases"
}

def read_text_from_github(url):
    """
    Reads text from a file hosted on GitHub.

    Args:
        url (str): The URL of the text file hosted on GitHub.

    Returns:
        str: The content of the text file as a string, or None if reading fails.
    """
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        return None
'''

index_to_topic = {
    0: "Healthcare Policy and Business",
    1: "Medical Research and Studies",
    2: "Entertainment and Sports",
    3: "Disease and Public Health",
    4: "Nutrition and Healthy Living"
}
@st.cache(allow_output_mutation=True)
def load_model_from_github(url):
    """
    Loads a model from a file hosted on GitHub.

    Args:
        url (str): The URL of the model file hosted on GitHub.

    Returns:
        object: The loaded model object, or None if loading fails.
    """
    response = requests.get(url)
    if response.status_code == 200:
        content = io.BytesIO(response.content)
        model = joblib.load(content)
        return model
    else:
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
    raw_data = extract_body(fetch_content(url))
    content = " ".join([p_tag.text.strip() for p_tag in raw_data])
    cleaned_data = clean_text(content)
    preprocessed_data = preprocess_text(cleaned_data)
    
    model_dictionary = Dictionary.load('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/dictionary.sav')
    transformed_data = model_dictionary.doc2bow(preprocessed_data)

    lda_model = load_model_from_github('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/lda_model.sav')
    topics_probability = lda_model.get_document_topics(transformed_data)
    topic_number = max(topics_probability, key=lambda x: x[1])[0]
    return index_to_topic.get(topic_number), preprocessed_data
