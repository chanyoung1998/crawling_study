import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getCompanyInformation(stocks,index,tab):

    pageString = crawl(stocks[tab][index])
    bsObj = BeautifulSoup(pageString, "html.parser")
    wrap = bsObj.find("div", {"id": "wrap"})
    middle = wrap.find("div", {"id": "middle"})
    content_wrap = middle.find("div", {"class": "content_wrap"})
    section_inner_sub = content_wrap.find("div", {"class": "section inner_sub"})
    coinfo_cp = section_inner_sub.find("iframe", {"id": "coinfo_cp"})

    return coinfo_cp["src"]

# Per
def getStockPER(url):
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    table = soup.find("table",[{"summary":"주요재무정보를 제공합니다."},{"class":"gHead01 all-width"}])

    print(table)



    PER = 0
    return PER

# 당기 순이익
def getStockNetIncome(url):
    pass

# 시가 총액
def getmarketCap(url):
    pass

# 부채 비율
def getDebtRatio(url):
    pass

# 당좌 비율
def getQuickRatio(url):
    pass

# 유보율
def getReserveRatio(url):
    pass

# 지분율
def getshareRatio(url):
    pass

# PBR
def getPBR(url):
    pass

def news(url):
    pass

stocks = pd.read_csv("./data/kospi_with_newtab.csv")
print(getStockPER(getCompanyInformation(stocks,0,"종목분석")))