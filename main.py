from parsing_market_cap import getSiseMarketSum
import tools


result = []
for page in range(2,3):
    list = getSiseMarketSum(0,page) # 0코스피,1코스닥
    result += list

tools.makejson("./data/kospi.json",result)
tools.jsontocsv("./data/kospi.json","./data/kospi.csv")

