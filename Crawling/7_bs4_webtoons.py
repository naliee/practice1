import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})
        # soup객체 전체에서 태그명:a, 속성값 class=title인 모든 요소

# 네이버 웹툰 전체 목록 가져오기
for cartoon in cartoons:
    print(cartoon.get_text())
