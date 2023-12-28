import requests
from bs4 import BeautifulSoup

# Send a request to the Yandex Images search page for Riga, Latvia
url = "https://yandex.com/images/search?text=Riga%2C+Latvia"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the image results container
results = soup.find("div", {"class": "image-results"})

# Extract the image URLs from the results container
image_urls = []
for result in results.find_all("div", {"class": "image-result"}):
    image_url = result.find("img")["src"]
    image_urls.append(image_url)

# Print the image URLs
print(image_urls)
