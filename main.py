import requests
from bs4 import BeautifulSoup
import os

def get_data(url):
    r = requests.get(url)
    return r.text

url = "https://en.wikipedia.org/wiki/Wikipedia:Featured_pictures" # Set URL to website you want to scrap images off of
html = get_data(url)
soup = BeautifulSoup(html, 'html.parser')

count = -1
for item in soup.find_all('img'):
    count += 1
    image = "https:" + item['src'] # For image sources without 'https:'

    try:
        if(item['src'][0] == "/" and item['src'][1] == "/"): # If it's an image without 'https:'
            print(image)
            response = requests.get(image)
        else:
            print(item['src']) # Any other image
            response = requests.get(item['src'])

        file = open("image[" + str(count) + "].jpg", "wb") # Creates .jpg for every image found
        file.write(response.content)
        file.close()

    except requests.exceptions.MissingSchema:
        print("missing URL\n")
        continue

    except requests.exceptions.InvalidSchema:
        print("invalid URL\n")
        continue