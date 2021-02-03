from selenium import webdriver
import time

                #현재 폴더에 있는 크롬드라이버를 쓰겠다
# 1. chromedriver로 웹 브라우저 객체 생성
# 2. 브라우저에서 해당 URL로 이동
browser = webdriver.Chrome("C:/Users/이벌브소프트/Desktop/PythonWorkspace/chromedriver.exe")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 로그인 창에 아이디, 비밀번호 입력 후 로그인
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")
browser.find_element_by_id("log.login").click()     # 로그인 버튼 클릭
time.sleep(3)   # 로딩 시간 기다리기 위해

# 4. 새로운 id 입력
#browser.find_element_by_id("id").send_keys("naver_id")  # 이전에 있던 데이터 뒤에 덧붙여짐
browser.find_element_by_id("id").clear()    # 해당 element의 내용 지우기
browser.find_element_by_id("id").send_keys("my_id")

# 5. html 정보 출력
print(browser.page_source)  # 현재 페이지의 모든 html소스 출력

# 6. 브라우저 종료
browser.quit()  # 전체 브라우저 종료