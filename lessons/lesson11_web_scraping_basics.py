"""
Lesson 11: Web Scraping Basics
Objective: Learn how to scrape data from websites using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

# Making a request to a website
url = "https://example.com"
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting specific elements
title = soup.title.string
print(f"Title of the page: {title}")  # Output: Title of the page: Example Domain

# Finding all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))  # Output: Prints all hyperlinks in the page.

# EXERCISE:
# 1. Write a script to scrape quotes from a quotes website and print them.
# 2. Extract the headlines from a news website and save them in a text file.
