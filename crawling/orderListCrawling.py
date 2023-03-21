from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'chromedriver.exe 경로'
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.get("https://mc.coupang.com/ssr/desktop/order/list")


def crawl_purchase_list():
    orderListXpath = '//*[@id="__next"]/div[2]/div[2]/div/div[4]/div'
    # //*[@id="__next"]/div[2]/div[2]/div # 주문내역 wrap
    orderList = driver.find_elements(By.XPATH, orderListXpath)

    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[1] # 일자 표시 영역 (무조건 첫번째)
    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[2] # 주문 물품 1
    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[3] # 주문 물품 2

    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[2]/div[1]
    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[2]/div[2]
    # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[2]/div[3]

    # 주문 목록 리스트 갯수
    orderListLen = len(orderList)
    print(orderListLen)

    for dayItems in orderList:
        print('')

        items = dayItems.find_elements(By.CSS_SELECTOR, ':scope > div')

        cnt = 1
        for item in items:
            print('---------------- START (' + str(cnt) + ') --------------------')
            print(item.text)
            print('----------------- END ----------------------')
            cnt += 1

        # //*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[1] # 일자 표시 영역 (무조건 첫번째)
        # 주문일자
        # orderDateSection = dayItems.find_elements(
        #     By.XPATH, orderListXpath)[1]
        # print(orderDateSection.text)
        # orderDate = orderDateSection.find_element(
        #     By.XPATH, itemXpath + '/div[1]/div[1]')
        # print(orderDate.text)

        # # 물품정보 ( 물품명, 배송상태 )
        # orderDateSection = orderItem.find_element(
        #     By.XPATH, itemXpath + '/div[2]')
        # print(orderDateSection.text)

        # # 구매 가격
        # price = orderItem.find_element(
        #     By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/div[3]/div/div[2]/div/div[2]/div/a[4]/div[1]/div/span[1]')
        # print(price.text)

        # # 구매 수량
        # price = orderItem.find_element(
        #     By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/div[3]/div/div[2]/div/div[2]/div/a[4]/div[1]/div/span[3]')
        # print(price.text)


crawl_purchase_list()
