import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def getPosts():

    # 크롬창(웹드라이버) 열기 
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe", options=options)

    # 우아한 형제들 기술블로그 접속하기 
    browser.get("https://techblog.woowahan.com/") 

    # 여러 페이지(999)에서 반복하기 
    for i in range(1):     
        # 시간 지연     
        time.sleep(1)  
        # 포스팅 데이터 수집      
        posts = browser.find_elements_by_class_name("item")

        for post in posts:         
            title = post.get_attribute("h1")
            print(title)

        #     #  포스팅 주소 데이터 수집         
        #     addr = post.find_elemenst_by_tag_name("a").text         
        #     print(title, "/", addr, "/", addr)     # 다음페이지 버튼 클릭 하기     # 다음페이지가 없는 경우(데이터 수집 완료) 에러 처리     
            
        # try:         
        #     nextpage = driver.find_element_by_css_selector("div.pagination")         
        #     nextpage.click()
        # except:      
        #     print("데이터 수집 완료.")         
        #     break 

    browser.close()

    return ''


