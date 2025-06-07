import requests
from bs4 import BeautifulSoup
from utils.helpers import fetch_page_content
from config.settings import TARGET_URLS

def main():
    for url in TARGET_URLS:
        print(f"Fetching content from: {url}")
        content = fetch_page_content(url)
        if content:
            parse_content(content)

def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Add parsing logic here
    print(soup.title.string)  # Example: print the title of the page

if __name__ == "__main__":
    main()