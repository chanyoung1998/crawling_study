
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import request
import bs4

driver = webdriver.Chrome()
driver.get("https://m.stock.naver.com/")
elem = driver.find_element_by_class_name("Nicon_search")
elem.click()

elem = driver.find_element_by_name("keyword_input")
elem.send_keys("005930",Keys.RETURN)

url = driver.