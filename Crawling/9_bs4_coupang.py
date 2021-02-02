import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# 주어진 url에 접속하여 정보를 가져온 뒤 해당 변수에 저장
res = requests.get(url, headers=headers)
res.raise_for_status()  # 제대로 접속하여 가져왔다면 200
soup = BeautifulSoup(res.text, "lxml") # lxml파서를 이용하여 정보를 text화 하고 Beautifulsoup객체로 변환하여 저장

# li태그이면서, class정보가 "search-product"로 시작하는 element들 전부 해당
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# for item in items:
#     print(item)

for item in items:

    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge"})
    if ad_badge:
        print("     <광고 상품 제외>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()  # rate가 없는 상품이 있을 수 있어(랜덤 광고) rate가 있을 시, (None이 아닐 시) get_text()
    else:
        print("     <평점 없는 상품 제외>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  # (26) 이런식으로 괄호가 포함되어 있는 형태
        rate_cnt = rate_cnt[1:-1]   # (빼고 다음에 나오는 첫 숫자(1번째 인덱스) ~ 끝에서 두번째 인덱스 - 끝자리는 포함x
        # print("리뷰 수", rate_cnt)
    else:
        print("     <평점 수 없는 상품 제외>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) > 100:
        # 애플 제품 제외
        if "Apple" in name:
            print("     <애플 상품 제외합니다>")
            continue
        print(name, price, rate, rate_cnt)

#print(items[0].find("div", attrs={"class":"name"}).get_text())

