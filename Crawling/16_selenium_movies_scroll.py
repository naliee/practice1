from selenium import webdriver
browser = webdriver.Chrome("C:/Users/이벌브소프트/Desktop/PythonWorkspace/chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 스크롤 내리기 - 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0, 2080)")  # 1920 x 1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 바뀐 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 현재 높이 == 이전 높이이면 총 스크롤이 끝났다는 얘기이므로 중단
    if curr_height == prev_height:
        break

    # 바뀐 높이(curr_height)를 prev_height에 저장 - break할 수 있도록
    prev_height = curr_height
print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

# res.text 대신 browser.page_source
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":["Vpfmgd"]})
                                            # value를 list형태로 부여 -> list중 하나에라도 해당되면 가져옴

for movie in movies:
    title = movie.find("div", attrs={"class":"vU6FJ p63iDd"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
        print("제목 : {}".format(title))
    else:
        print(title, "<할인되지 않은 영화>")
        continue

    # 할인 후 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"] #movie가 soup객체이기 때문에 soup문법대로 ["속석명"]-> value가져오기

    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()


