import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com"

def crawl(url):
    data = requests.get(url)
    return data.content

def parse(pageString):
    bs_obj = BeautifulSoup(pageString,"html.parser")

    # tabs_submenu = bs_obj.find("ul",{"class":"tabs_submenu tab_total_submenu"})
    tabs_submenu = bs_obj.find("ul", {"class": lambda x: x and 'tabs_submenu' in x.split()})
    print(tabs_submenu)
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
new_columns = {"종합정보","시세","차트","투자자별 매매동향","뉴스·공시","종목분석","종목토론실","전자공시","공매도현황"}
new_df = pd.DataFrame(columns=new_columns)

for i in range(25,31):
    list = getSpecificInfo(i)
    for j in range(len(list)):
        href = list[j]['href']
        new_df.loc[i,list[j]['tab_name']] = href

result = pd.concat([df,new_df],axis=1)
result.to_csv("./data/kospi_with_newtab.csv",sep=',',na_rep='NaN',columns=result.columns,index=False,encoding='utf-8')
