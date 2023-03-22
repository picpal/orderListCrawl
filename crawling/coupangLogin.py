from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

portNum = "9222"

# Get driver and open url
options = Options()

# headless 옵션 설정
options.add_argument("no-sandbox")

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

options.add_experimental_option("debuggerAddress", f"localhost:{portNum}")

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                       "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

driver = webdriver.Chrome(options=options)

loginUrl = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
# username = "novten2018@gmail.com"
# password = "123456789"

driver.get(loginUrl)

# Enter the login credentials
# username_field = driver.find_element(By.NAME, "email")
# password_field = driver.find_element(By.NAME, "password")
# username_field.send_keys(username)
# password_field.send_keys(password)

driver.find_element(By.CLASS_NAME, "_loginSubmitButton").click()

driver.implicitly_wait(10)

# driver.close()
