import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
'''
종목 사이트에 들어가서 각 탭에 있는 내용들을 크롤링해서 파싱
'''
url = "https://finance.naver.com"

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bs_obj = BeautifulSoup(pageString,"html.parser")

    tabs_submenu = bs_obj.find("ul",{"class":"tabs_submenu tab_total_submenu"})
    tabs = []
    for tab_li in tabs_submenu.find_all("li"):
        tab = tab_li.find("a")
        href = url + tab["href"]
        tab_name = tab.text
        tabs.append({"tab_name":tab_name,"href":href})

    return tabs

def geturl(ranking):
    return df['href'][ranking]


def getSpecificInfo(ranking):
    stock_url = geturl(ranking)
    pageString = crawl(stock_url)
    list = parse(pageString)
    return list


df = pd.read_csv("./data/kospi.csv")
new_columns = {"종합정보","시세","차트","투자자별 매매동향","뉴스,공시","종목분석","종목토론실","전자공시","공매도현황"}
new_df = pd.DataFrame(columns=new_columns)
for i in range(len(df)):
    list = getSpecificInfo(i)
    temp = []
    for j in range(len(list)):
        href = list[j]['href']
        temp.append(href)
    new_df.loc[i,new_columns] = temp

result = pd.concat([df,new_df],axis=1)
result.to_csv("./kospi_with_newtab.csv",sep=',',na_rep='NaN',columns=result.columns,index=True)
