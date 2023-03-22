from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

portNum = "9222"
chrome_options = Options()
chrome_options.add_experimental_option(
    "debuggerAddress", f"localhost:{portNum}")

driver = webdriver.Chrome(options=chrome_options)

# 주문내역 페이지 이동
driver.get("https://emart.ssg.com/")


def emart_order_list():
    result = []

    print('')


emart_order_list()
