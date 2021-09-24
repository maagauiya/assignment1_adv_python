import requests,json
temp=requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false").text
temp=json.loads(temp)
print("Enter the number up to which you want to filter3")
for i in range(0,int(input())):
    print(i+1,": ",temp[i]["name"]," ",temp[i]["market_cap"]," usd")