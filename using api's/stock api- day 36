import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "O90J46LH2347JMT5"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "fb3ba0d23b544f6ca8494fc69e146412"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API
}

news_parameters = {
    "apikey": NEWS_API,
    "qInTitle": COMPANY_NAME,
    "language": "en"
}

result = requests.get(url=STOCK_ENDPOINT, params=stock_parameters).json()
daily_results = result["Time Series (Daily)"]

sep11_close = float(daily_results['2023-09-11']['4. close'])
sep8_close = float(daily_results['2023-09-08']['4. close'])
sep7_close = float(daily_results['2023-09-07']['4. close'])

percentage = round(((abs(sep8_close-sep7_close))/((sep8_close+sep7_close)/2))*100)

if percentage > 5:
    result2 = requests.get(url=NEWS_ENDPOINT, params=news_parameters).json()
    data = result2['articles'][:3]
    print(data)
