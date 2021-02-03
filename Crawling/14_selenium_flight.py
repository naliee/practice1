from selenium import webdriver
# 로딩시간 대기용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:/Users/이벌브소프트/Desktop/PythonWorkspace/chromedriver.exe")
browser.maximize_window()   # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)    # URL로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 28일 선택
#browser.find_elements_by_link_text("27")[0].click()  # 이번 달, 다음 달 두 가지 달력이 있고 text가 27로 똑같으므로 먼저 등장하는 27을 지정
#browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번 달
# 다음 달 27일, 28일 선택
#browser.find_elements_by_link_text("27")[1].click()
#browser.find_elements_by_link_text("28")[1].click()

# 이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    # browser에 대해 10초간 기다린다(최대10초까지만). until EC(expected_conditions), XPATH란 조건(입력한 XPATH)에 해당하는 element가 위치할 때 까지
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)    # 첫 번째 결과 출력
finally:
    browser.quit()

# 검색 결과 가져오기
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)