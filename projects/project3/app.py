import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL to scrape
URL = "http://books.toscrape.com/"

# Step 2: Send a GET request to the URL
response = requests.get(URL)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    exit()

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "lxml")

# Step 4: Extract book titles and prices
books = soup.find_all("article", class_="product_pod")

# Step 5: Store data in a list
book_data = []
for book in books:
    title = book.h3.a["title"]  # Extract title using the title attribute of the <a> tag inside <h3>
    price = book.find("p", class_="price_color").text  # Extract price
    book_data.append({"Title": title, "Price": price})

# Step 6: Save the data to a CSV file
df = pd.DataFrame(book_data)
df.to_csv("books.csv", index=False)

print("Data has been successfully saved to 'books.csv'")
