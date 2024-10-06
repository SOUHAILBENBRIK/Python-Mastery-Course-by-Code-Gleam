"""
Lesson 11: Web Scraping Basics
Objective: Learn how to scrape data from websites using BeautifulSoup and Requests libraries.
"""
"Documentation https://pypi.org/project/beautifulsoup4/"

import requests
from bs4 import BeautifulSoup

# Step 1: Making a request to a website
url = "https://example.com"
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
except requests.exceptions.HTTPError as err:
    raise SystemExit(f"HTTP Error: {err}")
except requests.exceptions.RequestException as e:
    raise SystemExit(f"Request Error: {e}")

# Step 2: Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extracting specific elements - Title of the page
title = soup.title.string if soup.title else "No Title Found"
print(f"Title of the page: {title}")  # Output: Title of the page: Example Domain

# Step 4: Finding all links on the page
links = soup.find_all('a')
print("\nAll hyperlinks in the page:")
for link in links:
    print(link.get('href'))  # Output: Prints all hyperlinks in the page.

# Step 5: Extracting other HTML elements like paragraphs and headers
paragraphs = soup.find_all('p')
print("\nParagraphs in the page:")
for para in paragraphs:
    print(para.text)  # Print each paragraph's content

# Step 6: Using different BeautifulSoup methods for extraction
print("\nUsing CSS selectors to find elements:")
headers = soup.select('h1, h2, h3')  # Select headers of different levels using CSS selectors
for header in headers:
    print(header.text)

# Step 7: Handling pagination (if the website has multiple pages)
# Many sites have multiple pages, e.g., `/page/2/`, `/page/3/`, etc.
# Modify the URL pattern to scrape data across pages
print("\nScraping multiple pages (pagination example):")
for page in range(1, 4):  # Assume we want to scrape the first 3 pages
    paginated_url = f"https://example.com/page/{page}"
    response = requests.get(paginated_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_titles = soup.find_all('h2')  # Assuming the titles are in <h2> tags
    for title in page_titles:
        print(title.text)

# Step 8: Using custom headers to mimic a real browser (avoiding blocks)
print("\nUsing custom headers:")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print("Page reloaded with custom headers.")

# Step 9: Checking for the robots.txt file to respect scraping rules
robots_url = "https://example.com/robots.txt"
robots_response = requests.get(robots_url)
print(f"\nrobots.txt for {url}:\n{robots_response.text}")  # Output: Shows the robots.txt rules for scraping

# Step 10: Saving the extracted data to a text file
print("\nSaving links to a text file...")
with open("extracted_links.txt", "w") as file:
    for link in links:
        file.write(link.get('href') + "\n")

print("Links saved successfully to 'extracted_links.txt'.")

# EXERCISES:
# 1. Write a script to scrape quotes from a quotes website (e.g., http://quotes.toscrape.com/) and print them.
#    - Try extracting the quote text and author names.
#    - Modify your script to handle pagination and collect data from multiple pages.
# 
# 2. Extract the headlines from a news website and save them in a text file.
#    - Identify the main tags containing the headlines (e.g., <h2> or <h3>) using browser inspection tools.
#
# 3. Use the `select` method to extract elements using CSS selectors, e.g., all buttons on the page.
#    - Try using selectors like 'button', '.class-name', '#id-name'.
#
# 4. Write a script that navigates through multiple pages of a website and collects data across them.
#    - Consider websites like blogs that have "/page/1", "/page/2" in their URLs.
#
# 5. BONUS: Try using the `requests.Session` object to maintain a session while scraping a site with login.
#    - This helps handle websites that require cookies and login data for scraping.
