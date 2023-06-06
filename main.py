import requests
from twilio.rest import Client

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()['Time Series (Daily)']

data_list = list(data.values())
yesterday_closing_price = float(data_list[0]['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

daily_price_move_percent = (yesterday_closing_price - day_before_yesterday_closing_price) / day_before_yesterday_closing_price * 100
abs_percent = abs(daily_price_move_percent)

if abs_percent > 5:
    news_params = {
        'q': COMPANY_NAME,
        'sortby': 'relevancy',
        'apiKey': NEWS_API_KEY,
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()['articles']
    three_articles = articles[:3]

    news = f"\n{STOCK}: {'🔺' if daily_price_move_percent>0 else '🔻'}{round(abs_percent, 2)}%\n"
    for article in three_articles:
        news += f"\nHeadline: {article['title']}\nBrief: {article['description']}\n\n"

    message = client.messages.create(
        body=news,
        from_='YOUR_TWILIO_PHONE_NUMBER',
        to='YOUR_DESTINATION_PHONE_NUMBER'
    )
    print(message.status)

