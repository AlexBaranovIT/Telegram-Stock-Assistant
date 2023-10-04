import telebot
import yfinance as yf

# Replace with your Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Mapping of company names to their stock tickers
COMPANY_TO_TICKER = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'GOOGLE': 'GOOGL',
    'AMAZON': 'AMZN',
    # ... add more companies and their tickers as needed
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a stock ticker (e.g., AAPL for Apple) or a company name, and I'll give you its current price.")

@bot.message_handler(func=lambda message: True)
def send_stock_price(message):
    name_or_ticker = message.text.upper()
    ticker = COMPANY_TO_TICKER.get(name_or_ticker, name_or_ticker)  # Get the ticker from the mapping or use the provided text

    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'][0]
        if name_or_ticker in COMPANY_TO_TICKER:
            bot.reply_to(message, f"The current price of {name_or_ticker} ({ticker}) is ${price:.2f}")
        else:
            bot.reply_to(message, f"The current price of {ticker} is ${price:.2f}")
    except Exception as e:
        bot.reply_to(message, f"Sorry, I couldn't fetch the price for {ticker}. Please try another stock ticker or company name.")

bot.polling()
