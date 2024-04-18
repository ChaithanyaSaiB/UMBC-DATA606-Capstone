import joblib
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from gensim.corpora.dictionary import Dictionary
import streamlit as st
import io

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('words')

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

def predict(url):
    """
    Predicts the topic of a news article from a given URL.

    Args:
        url (str): The URL of the news article.

    Returns:
        tuple: A tuple containing the predicted topic and the filtered data.
    """
    raw_data = extract_body(fetch_content(url))
    content = " ".join([p_tag.text.strip() for p_tag in raw_data])
    tokenized_data = word_tokenize(content)
    lemmatized_data = lowercase_words_and_lemmatize(tokenized_data)
    filtered_data = remove_non_alphabetic_and_custom_stopwords(stopwords_removal(lemmatized_data))
    
    model_dictionary = Dictionary.load('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/dictionary.sav')
    transformed_data = model_dictionary.doc2bow(filtered_data)

    lda_model = load_model_from_github('https://raw.githubusercontent.com/ChaithanyaSaiB/UMBC-DATA606-Capstone/main/app/lda_model.sav')
    topics_probability = lda_model.get_document_topics(transformed_data)
    topic_number = max(topics_probability, key=lambda x: x[1])[0]
    return index_to_topic.get(topic_number), filtered_data
