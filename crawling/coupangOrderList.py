from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

portNum = "9222"

chrome_options = Options()
chrome_options.add_experimental_option(
    "debuggerAddress", f"localhost:{portNum}")

driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                       "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

# 주문내역 페이지 이동
driver.get("https://mc.coupang.com/ssr/desktop/order/list")


def coupang_order_list():
    result = []

    try:
        # 브라우저를 최대 10초까지 기다린다. (xpath의 값이 나올때까지)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[4]'))
        )
    finally:
        driver.quit()

    # 주문내역 wrapper
    order_list_xpath = '//*[@id="__next"]/div[2]/div[2]/div/div[4]/div'
    order_list = driver.find_elements(By.XPATH, order_list_xpath)

    # validate
    if order_list == 'null' and len(order_list) < 1:
        return result

    # parsing
    for day_items in order_list:
        items = day_items.find_elements(By.CSS_SELECTOR, ':scope > div')

        item_count = 1
        for item in items:
            # 주문일자
            if item_count == 1:
                order_date = item.find_elements(
                    By.CSS_SELECTOR, ':scope > div')[0].text

                # date parsing
                date_regex = r"\d{4}\.\s\d{1,2}\.\s\d{1,2}"
                matches = re.findall(date_regex, order_date)

                if matches:
                    date = matches[0]
                    print(date)
                else:
                    print("No date found in text")

            # 주문일자의 주문물품목록
            if item_count > 1:
                order = item.text.split('\n')

                # not found goods
                if len(order) == 1:
                    continue

                # split goods info
                product_info = order[2]
                price_info = order[3]
                quantity_info = order[4]

                # Extract the price using regular expressions
                price_pattern = r'([\d,]+) 원'
                match = re.search(price_pattern, price_info)
                price = match.group(1).replace(',', '')

                # Extract the quantity using regular expressions
                quantity_pattern = r'(\d+) 개'
                match = re.search(quantity_pattern, quantity_info)
                quantity = match.group(1)

                # Create an order dictionary
                order_summary = {
                    'product_name': product_info,
                    'quantity': quantity,
                    'price': price
                }

                print(", 물품 : " + product_info)
                print(", 수량 : " + quantity)
                print(", 가격 : " + price)

            item_count += 1

    return result


coupang_order_list()
