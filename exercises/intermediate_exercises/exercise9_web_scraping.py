# Problem: Web Scraping
# Question: Write a script to scrape data from a website and extract specific information.








import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [title.get_text() for title in soup.find_all('h2')]

# Example usage
# print(scrape_website("https://example.com"))
