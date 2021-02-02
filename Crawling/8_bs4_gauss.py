import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목, 링크 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0 # 전체 평점
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate2 = cartoon.find("strong").get_text()  # 이 식에서 cartoon.strong과 똑같이 작동
    rate = cartoon.strong.get_text()
    print(rate)
    total_rates += float(rate) # 현재 평점 정보는 string이므로 float-실수형 으로 변환
print("전체 점수 : ", round(total_rates, 2))
print("평균 점수 : ", round(total_rates / len(cartoons), 2))


