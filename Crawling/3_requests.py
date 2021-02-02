import requests
res = requests.get("http://google.com")    # 해당 URL에 접속하여 정보 가져옴
res.raise_for_status()  # 문제발생 시 오류코드 반환 후 프로그램 종료

# 가져 온 정보를 file로 생성
with open("google.html", "w", encoding="utf8") as f:
    f.write(res.text)

print(res.text)