from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")   # 크기 설정. 해당 크기에 맞춰 브라우저에서 스크래핑 실행
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")


browser = webdriver.Chrome("C:/Users/이벌브소프트/Desktop/PythonWorkspace/chromedriver.exe", options=options)
browser.maximize_window()

# User Agent값 Headless로 가져오기
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
# 결과: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4324.104 Safari/537.36
browser.quit()

