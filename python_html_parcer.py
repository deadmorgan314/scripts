import requests
import sys
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/"
find = "a"
filename = "file.csv"
to_get = "href"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
links = soup.find_all(find)
sys.stdout = open(filename, "w")
for link in links:
    print(link.get(to_get))
sys.stdout.close()


