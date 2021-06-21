from parsing_market_cap import getSiseMarketSum
import tools
import pandas as pd

result = []
for page in range(2,3):
    list = getSiseMarketSum(0,page) # 0코스피,1코스닥
    result += list

tools.makejson("./data/kospi.json",result)
tools.jsontocsv("./data/kospi.json","./data/kospi.csv")

new_columns = {"종합정보","시세","차트","투자자별 매매동향","뉴스·공시","종목분석","종목토론실","전자공시","공매도현황"}
new_df = pd.DataFrame(columns=new_columns)


from data_processing import getSpecificInfo
from data_processing import stocks

for i in range(len(stocks)):
    list = getSpecificInfo(i)
    for j in range(len(list)):
        href = list[j]['href']
        new_df.loc[i,list[j]['tab_name']] = href

result = pd.concat([stocks, new_df], axis=1)
result.to_csv("./data/kospi_with_newtab.csv",sep=',',na_rep='NaN',columns=result.columns,index=False,encoding='utf-8')

import stock
print(result.columns)

