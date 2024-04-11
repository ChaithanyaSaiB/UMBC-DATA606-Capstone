
import joblib
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('words')
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.corpora.dictionary import Dictionary

# Function to fetch the content from a URL
def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print("Error fetching content:", e)
        return None

# Function to extract body content from HTML using BeautifulSoup
def extract_body(html_content):
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
  # Define pattern for special characters
  pattern = r'[-\s]'

  for word in word_list:
    if re.search(r'[-\s]', word):
      # Split the string using the pattern
      substrings = re.split(pattern, word)

      # Remove empty substrings
      substrings = [substr for substr in substrings if substr]

      word_list.remove(word)
      word_list.extend(substrings)
  return word_list

def lowercase_words_and_lemmatize(word_list):
    # Convert words to lowercase
    word_list_lower = [word.lower() for word in word_list]

    # Tag POS for each word
    pos_tags = nltk.pos_tag(word_list_lower)

    # Map POS tags to WordNet POS tags
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
            return wordnet.NOUN  # Default to noun if POS tag not found

    # Lemmatize words using correct POS tags
    lemmatized_words = []

    lemmatizer = WordNetLemmatizer()
    for word, tag in pos_tags:
        pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos=pos)
        lemmatized_words.append(lemma)

    return lemmatized_words

parts_of_speech_to_remove = ['DT', 'IN', 'PRP', 'PRP$', 'CC', 'VB', 'JJ']

def stopwords_removal(word_list):
  # Tag words with their parts of speech
  tagged_words = nltk.pos_tag(word_list)

  # Get a list of common English stopwords
  stop_words = set(stopwords.words('english'))

  f = open('custom stopwords.txt','r')
  custom_stopwords = [word.strip() for word in f.readlines()]
  f.close()

  return [word for word, pos in tagged_words if pos not in parts_of_speech_to_remove and word not in stop_words and word not in custom_stopwords]

def remove_non_alphabetic_and_custom_stopwords(word_list):
    english_words = set(nltk.corpus.words.words())

    # Remove non-alphabetic characters and filter out empty strings
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

def predict(url):
  raw_data = extract_body(fetch_content(url))
  content = " ".join([p_tag.text.strip() for p_tag in raw_data])
  tokenized_data = word_tokenize(content)
  lemmatized_data = lowercase_words_and_lemmatize(tokenized_data)
  filtered_data = remove_non_alphabetic_and_custom_stopwords(stopwords_removal(lemmatized_data))
    
  model_dictionary = Dictionary.load('dictionary.sav')
  transformed_data = model_dictionary.doc2bow(filtered_data)

  lda_model = joblib.load("lda_model.sav")
  topics_probability = lda_model.get_document_topics(transformed_data)
  topic_number = max(topics_probability, key=lambda x: x[1])[0]
  return index_to_topic.get(topic_number)
