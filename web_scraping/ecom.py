import requests
from bs4 import BeautifulSoup

url = "https://breakout.com.pk/collections/men-shirts"

r = requests.get(url)
soup = BeautifulSoup(r, 'html.parser')

shirts= soup.find_all('li', class_="product")
print(shirts)