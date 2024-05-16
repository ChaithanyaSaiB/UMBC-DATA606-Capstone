import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

# Function to fetch content from a URL
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

# Apply web scraping to extract content and store it in a new column
def extract_content_with_progress(url_list):
    content_list = []
    for url in tqdm(url_list, desc='Extracting content'):
        content = extract_body(fetch_content(url))
        content_list.append(content)
    return content_list