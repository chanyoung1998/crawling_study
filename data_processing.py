import pandas as pd
import requests
from bs4 import BeautifulSoup

stocks = pd.read_csv("./data/kospi.csv")
url = "https://finance.naver.com"

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bs_obj = BeautifulSoup(pageString,"html.parser")

    # tabs_submenu = bs_obj.find("ul",{"class":"tabs_submenu tab_total_submenu"})
    tabs_submenu = bs_obj.find("ul", {"class": lambda x: x and 'tabs_submenu' in x.split()})
    #print(tabs_submenu)
    tabs = []

    for tab_li in tabs_submenu.find_all("li"):
        tab = tab_li.find("a")
        href = url + tab["href"]
        tab_name = tab.text
        tabs.append({"tab_name":tab_name,"href":href})

    return tabs

def geturl(ranking):
    return stocks['href'][ranking]


def getSpecificInfo(ranking):
    stock_url = geturl(ranking)
    pageString = crawl(stock_url)
    list = parse(pageString)
    return list


