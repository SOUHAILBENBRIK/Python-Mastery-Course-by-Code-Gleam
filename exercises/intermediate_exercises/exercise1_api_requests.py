# Problem: API Requests
# Question: Make a GET request to a public API and display the JSON response.








import requests

def fetch_data_from_api(url):
    response = requests.get(url)
    return response.json()

# Example usage
# print(fetch_data_from_api("https://api.github.com"))
