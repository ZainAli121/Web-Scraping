import requests
from bs4 import BeautifulSoup

url = "https://www.levi.com/US/en_US/search/T-shirts"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())


# In Progress.....................