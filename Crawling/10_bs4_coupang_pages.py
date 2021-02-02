import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# 1페이지부터 5페이지까지 가져오기
for i in range(1, 6):
    print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    # 주어진 url에 접속하여 정보를 가져온 뒤 해당 변수에 저장
    res = requests.get(url, headers=headers)
    res.raise_for_status()  # 제대로 접속하여 가져왔다면 200
    soup = BeautifulSoup(res.text, "lxml") # lxml파서를 이용하여 정보를 text화 하고 Beautifulsoup객체로 변환하여 저장

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        ad_badge = item.find("span", attrs={"class":"ad-badge"})
        if ad_badge:
            #print("     <광고 상품 제외>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()

        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()  # rate가 없는 상품이 있을 수 있어(랜덤 광고) rate가 있을 시, (None이 아닐 시) get_text()
        else:
            #print("     <평점 없는 상품 제외>")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]  # (26) 이런식으로 괄호가 포함되어 있는 형태
        else:
            #print("     <평점 수 없는 상품 제외>")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) > 100:
            if "Apple" in name:
                #print("     <애플 상품 제외>")
                continue
            #print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100)  # 줄긋기


