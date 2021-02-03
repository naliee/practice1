import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
# 접속하는 사용자의 header정보에 따라 google에서는 서로 다른 정보를 return
res = requests.get(url, headers=headers)    # user agent설정이 없으면 google원어 주소로 접속하여 다른 html값을 받아 옴
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

for movie in movies:
    title = movie.find("div", attrs={"class":"vU6FJ p63iDd"}).get_text()
    print(title)
