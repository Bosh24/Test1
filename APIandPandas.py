import requests
import pandas as pd


# API endpoint
url = "https://www.alphavantage.co/query"
params = {'function': 'NEWS_SENTIMENT', 
'tickers' : 'AAPL', 
'apikey': 'E7KZJRLBNDOJQAY1'}
response = requests.get(url,params=params)
data = response.json()
feed = data.get("feed", [])
df = pd.DataFrame(feed)[["title", "summary"]]

df = df.reset_index(drop=True)

print(df.head(10))
