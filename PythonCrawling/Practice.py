import requests
from bs4 import BeautifulSoup

url = "https://arxiv.org/search/?query=python&searchtype=all&source=header"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print(res.text)