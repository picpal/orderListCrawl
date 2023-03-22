from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os

portNum = "9222"
os.system("taskkill /IM chrome.exe /F")  # 열려 있는 chrome.exe 모두 종료
os.startfile(f"runChromeDebug{portNum}.bat")  # 디버그 모드로 chrome 실행

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'

if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)
