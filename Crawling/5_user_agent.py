import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

res = requests.get(url, headers=headers)    # 해당 URL에 접속하여 정보 가져옴
#res.raise_for_status()

with open("C:/Users/이벌브소프트/Desktop/PythonWorkspace/Crawling/nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
