import requests
import pandas as pd
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getStockurl(stocks,index,tab):
    return stocks[tab][index]

# Per
def getStockPER(url):
    pageString = crawl(url)
    bsObj = BeautifulSoup(pageString, "html.parser")
    wrap = bsObj.find("div", {"id":"wrap"})
    middle = wrap.find("div",{"id":"middle"})
    content_wrap = middle.find("div",{"class":"content_wrap"})
    print(content_wrap)
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
print(getStockPER(getStockurl(stocks,0,"종목분석")))