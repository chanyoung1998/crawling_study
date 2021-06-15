import parsing
import json

result = []
for page in range(1,2):
    list = parsing.getSiseMarketSum(0,page) # 0코스피,1코스닥
    result += list

print(result)

file = open("./data/kospi.json","w+")
file.write(json.dumps(result))

