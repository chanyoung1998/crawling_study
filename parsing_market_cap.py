import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


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


    driver = webdriver.Chrome("./chromedriver.exe")
    code_url2 = href
    driver.get(code_url2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 동종업계 PER
    fild_per = soup.select_one('#tab_con1 > div:nth-child(6) > table > tbody > tr.strong > td > em').text

    # 차트 테이블
    html2 = requests.get(code_url2)
    table = pd.read_html(html2.text)
    df = table[3]
    driver.implicitly_wait(3)

    # 배당 수익률
    dividend_yield = df.iloc[14, 3]

    # _pbr
    pbr = df.iloc[12, 3]

    # 현재 PER
    stock_per = df.iloc[10, 3]

    # 미래 PER
    potential_per = df.iloc[10, 4]

    # 당기순이익
    Net_income2017 = df.iloc[2, 1]
    Net_income2018 = df.iloc[2, 2]
    Net_income2019 = df.iloc[2, 3]
    Net_income2020 = df.iloc[2, 4]

    # 부채비율
    Deb_ratio2017 = df.iloc[6, 1]
    Deb_ratio2018 = df.iloc[6, 2]
    Deb_ratio2019 = df.iloc[6, 3]
    Deb_ratio2020 = df.iloc[6, 4]

    # 당좌비율
    Quick_ratio2017 = df.iloc[7, 1]
    Quick_ratio2018 = df.iloc[7, 2]
    Quick_ratio2019 = df.iloc[7, 3]
    Quick_ratio2020 = df.iloc[7, 4]

    # 유보율
    Reserve_ratio2017 = df.iloc[8, 1]
    Reserve_ratio2018 = df.iloc[8, 2]
    Reserve_ratio2019 = df.iloc[8, 3]
    Reserve_ratio2020 = df.iloc[8, 4]

    driver.implicitly_wait(3)

    return {"순위":rank,"주식명":name,"href":href,"현재가":nowprice,"시가총액":totalPrice,"거래량":volume,'PER':stock_per,'미래 PER':potential_per,'동일업종PER':fild_per,'시가배당률':dividend_yield,'PRB':pbr,
                          '당기순이익2017':Net_income2017,'당기순이익2018':Net_income2018,'당기순이익2019':Net_income2019,'당기순이익2020':Net_income2020,'부채비율2017':Deb_ratio2017,'부채비율2018':Deb_ratio2018,'부채비율2019':Deb_ratio2019,'부채비율2020':Deb_ratio2020,
                         '당좌비율2017':Quick_ratio2017,'당좌비율2018':Quick_ratio2018,'당좌비율2019':Quick_ratio2019,'당좌비율2020':Quick_ratio2020,
                         '유보율2017':Reserve_ratio2017,'유보율2018':Reserve_ratio2018,'유보율2019':Reserve_ratio2019,'유보율2020':Reserve_ratio2020}

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

