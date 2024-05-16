import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from fake_useragent import UserAgent
'''
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
'''

# Function to fetch content from a URL
def fetch_content(url):
    # Create a UserAgent instance
    ua = UserAgent()
    try:
        # Define user-agent header using a random user agent
        headers = {'User-Agent': ua.random}

        # Create a session to handle cookies and maintain connection state
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=4, allow_redirects=True)
            response.raise_for_status()  # Raise an error for 4xx and 5xx status codes
            final_url = response.url  # Get the final URL after following redirects
            website_name = get_website_name(final_url)
            return (response.text, website_name)
    except Exception as e:
        print("Error fetching content:", e)
        return (None, None)

# Function to extract website name from URL
def get_website_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Function to extract body content from HTML using BeautifulSoup
def extract_body(html_content_with_website_name):
    html_content, website_name = html_content_with_website_name
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        if soup:
            if website_name == 'www.cnn.com':
                article_body = soup.findAll('p', class_='paragraph')
            elif website_name == 'www.health.usnews.com':
                article_body = soup.findAll('p')
            elif website_name == 'www.latimes.com':
                article_body = soup.findAll('p')
            elif website_name == 'www.npr.org':
                storytext_div = soup.find('div', id='storytext')
                if storytext_div:
                    article_body = storytext_div.find_all('p')
                else:
                    article_body = None
            elif website_name == 'www.cbc.ca':
                storytext_div = soup.find('div', class_='story')
                if storytext_div:
                    article_body = storytext_div.find_all('p')
                else:
                    article_body = None
            else:
                article_body = None

            if article_body:
                return article_body
            else:
                return None
        else:
            return None
    else:
        return None

