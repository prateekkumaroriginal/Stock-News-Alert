# Stock-News-Alert
This Python program retrieves daily stock price data from Alpha Vantage and sends news alerts via SMS using Twilio. It checks the percentage change in the stock price and sends news articles if the change exceeds 5%.

## Setup
Clone the repository or download the Python file.<br>
Install the required libraries.<br>
Obtain the necessary API keys: -<br>
Alpha Vantage: Sign up for an API key at [https://www.alphavantage.co/](https://www.alphavantage.co/).<br>
News API: Register for an API key at [https://newsapi.org/](https://newsapi.org/).<br>
Open the Python file in a text editor.<br><br>

Replace the placeholder values in the following lines with your own API keys and phone numbers:<br>
`account_sid = 'YOUR_TWILIO_ACCOUNT_SID'`<br>
`auth_token = 'YOUR_TWILIO_AUTH_TOKEN'`<br>
`STOCK_API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'`<br>
`NEWS_API_KEY = 'YOUR_NEWS_API_KEY'`<br>
`from_='+YOUR_TWILIO_PHONE_NUMBER'`<br>
`to='+YOUR_DESTINATION_PHONE_NUMBER'`<br><br>

Save the file.

## Usage
1. Run the Python script in your terminal or IDE.
2. The program will retrieve the daily stock price data for the specified stock symbol (e.g., TSLA) using the Alpha Vantage API.
3. It will calculate the percentage change in the stock price and check if it exceeds 5%.
4. If the change is significant, it will fetch relevant news articles related to the company using the News API.
5. The program will then send an SMS alert containing the stock symbol, percentage change, and headlines of the top three news articles using Twilio.
6. Check your phone for the received SMS alert.

## Note
This program can be modified to monitor different stocks by changing the `STOCK` and `COMPANY_NAME` variables in the Python code.

## Tech Stack
Language: Python<br>
Libraries: "requests", "twilio"

## API's
<a href="https://www.alphavantage.co/">Alpha Vantage</a><br>
<a href="https://newsapi.org/">News API</a><br>
<a href="https://www.twilio.com/docs/sms">Twilio</a><br>
