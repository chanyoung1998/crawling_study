import requests
from bs4 import BeautifulSoup
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getStockInfo(tr):
    tds = tr.findAll("td")
    rank = tds[0].text
    print(tds)
    return {"rank":rank}

def parse(pageString):
    bsObj = BeautifulSoup(pageString,"html.parser")
    box_type_l = bsObj.find("div",{"class":"box_type_l"})
    type_2 = box_type_l.find("table",{"class":"type_2"})
    t_body = type_2.find("tbody")
    trs = t_body.findAll("tr")
    tr = trs[1]
    stock_info = getStockInfo(tr)
    print(stock_info)
    return []

def getSiseMarketSum(sosok,page):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}".format(sosok, page)
    pageString = crawl(url)
    list = parse(pageString)
    return list

result = []
for page in range(2,3):
    list = getSiseMarketSum(1,page) # 0코스피,1코스닥
    result.append(list)

print(result)