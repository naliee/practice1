import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# 혹시 모를 헤더 설정
options = webdriver.ChromeOptions()

browser = webdriver.Chrome("C:/Users/이벌브소프트/Desktop/PythonWorkspace/chromedriver.exe")  # chromedriver로 웹 브라우저 객체 생성
url = "https://arxiv.org/search/?query=python&searchtype=all&source=header"
browser.get(url)    # 브라우저에서 URL로 이동

soup = BeautifulSoup(browser.page_source, "lxml")

results = soup.find_all("li", attrs={"class":"arxiv-result"})
ps = ""
other = ""
for result in results:
    title = result.find("p", attrs={"class": "title is-5 mathjax"}).get_text().strip()
    link = result.find("p", attrs={"class": "list-title is-inline-block"}).find("a")["href"]



    # pdf, ps, other
    pdf = result.find("p", attrs={"class": "list-title is-inline-block"}).find("span").find_all("a")[0]["href"]
    link_cnt = result.find("p", attrs={"class": "list-title is-inline-block"}).find("span").get_text().count(",")
    if link_cnt == 1:
        other = result.find("p", attrs={"class": "list-title is-inline-block"}).find("span").find_all("a")[1]["href"]
    elif link_cnt > 1:
        ps = result.find("p", attrs={"class": "list-title is-inline-block"}).find("span").find_all("a")[1]["href"]
        other = result.find("p", attrs={"class": "list-title is-inline-block"}).find("span").find_all("a")[2]["href"]

    # aut_cnt = len(result.find("p", attrs={"class":"authors"}).find_all("a"))
    # for i in range(0, aut_cnt):
    #     authors = result.find("p", attrs={"class":"authors"}).find_all("a")[i].get_text()
    # abstract = result.find()

    print(title, link_cnt, pdf, ps, other)




