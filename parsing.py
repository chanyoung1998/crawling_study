import requests
from bs4 import BeautifulSoup


def crawl(url):
    data = requests.get(url)
    #print(data)
    return data.content

def getStockInfo(tr):
    tds = tr.findAll("td")
    rank = tds[0].text
    aTag = tds[1].find("a")
    href = "https://finance.naver.com" + aTag["href"]
    name = aTag.text
    nowprice = tds[2].text
    totalPrice = tds[6].text
    volume = tds[9].text
    #print(tds)
    return {"rank":rank,"name":name,"href":href,"code":href[20:],"nowPrice":nowprice,"totalPrice":totalPrice,"volume":volume}

def parse(pageString,sosok):
    bsObj = BeautifulSoup(pageString,"html.parser")
    box_type_l = bsObj.find("div",{"class":"box_type_l"})
    type_2 = box_type_l.find("table",{"class":"type_2"})
    t_body = type_2.find("tbody")
    trs = t_body.findAll("tr")

    if sosok == 1:
        sosok = "코스닥"
    elif sosok == 0:
        sosok = "코스피"

    stockInfos = []
    for tr in trs[1:]:
        try:
            stock_info = getStockInfo(tr)
            stock_info["sosok"] = sosok
            stockInfos.append(stock_info)
        except Exception as e:
            #print("error")
            pass

    return stockInfos

def getSiseMarketSum(sosok,page):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}".format(sosok, page)
    pageString = crawl(url)
    list = parse(pageString,sosok)
    return list

