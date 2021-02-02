import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# requests로 가져온 html문서를 lxml parser를 통해 Beautifulsoup 객체로 만든 것
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)   # soup객체가 가진 내용 중 가장 먼저 등장하는 a 반환
# print(soup.a.attrs)     # a가 가진 속성들
# print(soup.a["href"])   # a의 href속성이 가진 value값 리턴

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # rank1에서 a element만 출력 - soup객체에서 추출한 정보도 soup객체처럼 사용 가능
# rank2 = rank1.find_next_siblings("li")

webtoon = soup.find("a", text="참교육-14화") # text: 시작-종료 태그 사이의 content
