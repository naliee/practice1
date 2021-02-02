import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

# 주어진 url에 접속하여 정보를 가져온 뒤 해당 변수에 저장
res = requests.get(url, headers=headers)
res.raise_for_status()  # 제대로 접속하여 가져왔다면 200
soup = BeautifulSoup(res.text, "lxml") # lxml파서를 이용하여 정보를 text화 하고 Beautifulsoup객체로 변환하여 저장

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
for item in items:
    print(item)
                    # li태그이면서, class정보가 "search-product"로 시작하는 element들 전부 해당
for item in items:
    name = item.find("div", attrs={"claes":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"}).get_text()
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()

    print(name, price, rate, rate_cnt)

#print(items[0].find("div", attrs={"class":"name"}).get_text())

