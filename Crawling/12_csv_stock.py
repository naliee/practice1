import csv  # csv파일로 저장하기 위해 csv import
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "C:/Users/이벌브소프트/Desktop/PythonWorkspace/Crawling/시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")    # newline - 따로 설정해주지 않을 시 엔터 처리, 불필요한 엔터 제거
                            # 엑셀용 한글 인코딩 utf-8-sig
writer = csv.writer(f)

# 컬럼 타이틀 넣기

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # table태그, class가 type_2 - 순위정보 테이블 / 해당 테이블에서 tbody 내의 모든 tr(테이블 로우) - 리스트 형태로 저장됨
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")

        # 공백, 줄바꿈 처리 tr 빼기 (공백, 줄바꿈 로우의 경우 td가 하나 이하만 있음)
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]   # 한 줄 for문
                                # .strip() 불필요한 정보 제거
        # for column in columns
        #   data = column.get_text()
        writer.writerow(data)

