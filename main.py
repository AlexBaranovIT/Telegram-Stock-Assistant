# pip install telebot
import telebot
# pip install yfinance
import yfinance as yf
# to connect to monitor UptimeRobot
from keepalive import keep_alive
 
# Replace with your Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

keep_alive() 
 
# Mapping of company names to their stock tickers
COMPANY_TO_TICKER = {
    'APPLE': 'AAPL',
    'MICROSOFT': 'MSFT',
    'GOOGLE': 'GOOGL',
    'AMAZON': 'AMZN',
    'FACEBOOK': 'FB',
    'TESLA': 'TSLA',
    'NETFLIX': 'NFLX',
    'ALIBABA': 'BABA',
    'BERKSHIRE HATHAWAY': 'BRK.A',
    'JOHNSON & JOHNSON': 'JNJ',
    'JPMORGAN CHASE': 'JPM',
    'EXXON MOBIL': 'XOM',
    'VISA': 'V',
    'WALMART': 'WMT',
    'BANK OF AMERICA': 'BAC',
    'PROCTER & GAMBLE': 'PG',
    'MASTERCARD': 'MA',
    'DISNEY': 'DIS',
    'CISCO': 'CSCO',
    'VERIZON': 'VZ',
    'CHEVRON': 'CVX',
    'COCA-COLA': 'KO',
    'INTEL': 'INTC',
    'HOME DEPOT': 'HD',
    'PFIZER': 'PFE',
    'PEPSICO': 'PEP',
    'MCDONALD\'S': 'MCD',
    '3M': 'MMM',
    'IBM': 'IBM',
    'NIKE': 'NKE',
    'MERCK': 'MRK',
    'GOLDMAN SACHS': 'GS',
    'BOEING': 'BA',
    'AMERICAN EXPRESS': 'AXP',
    'AT&T': 'T',
    'STARBUCKS': 'SBUX',
    'ORACLE': 'ORCL',
    'UNITEDHEALTH': 'UNH',
    'CITIGROUP': 'C',
    'GENERAL ELECTRIC': 'GE',
    'MORGAN STANLEY': 'MS',
    'QUALCOMM': 'QCOM',
    'FORD': 'F',
    'ABBOTT LABORATORIES': 'ABT',
    'GENERAL MOTORS': 'GM',
    'AIG': 'AIG',
    'DELL': 'DELL',
    'CATERPILLAR': 'CAT',
    'DU PONT': 'DD',
    'TARGET': 'TGT',
    'TIME WARNER': 'TWX',
    'METLIFE': 'MET',
    'LOCKHEED MARTIN': 'LMT',
    'AMERICAN AIRLINES': 'AAL',
    'DELTA AIR LINES': 'DAL',
    'SOUTHWEST AIRLINES': 'LUV',
    'GILEAD SCIENCES': 'GILD',
    'RAYTHEON': 'RTN',
    'HONEYWELL': 'HON',
    'COLGATE-PALMOLIVE': 'CL',
    'TEXAS INSTRUMENTS': 'TXN',
    'MARRIOTT': 'MAR',
    'MONDELEZ': 'MDLZ',
    'CONOCOPHILLIPS': 'COP',
    'FEDEX': 'FDX',
    'SCHLUMBERGER': 'SLB',
    'SYMANTEC': 'SYMC',
    'NORTHROP GRUMMAN': 'NOC',
    'DOW CHEMICAL': 'DOW',
    'PHILIP MORRIS': 'PM',
    'BRISTOL-MYERS SQUIBB': 'BMY',
    'GOLDMAN SACHS GROUP': 'GS',
    'HALLIBURTON': 'HAL',
    'KRAFT HEINZ': 'KHC',
    'MORGAN STANLEY': 'MS',
    'BLACKROCK': 'BLK',
    'AMGEN': 'AMGN',
    'FREEPORT-MCMORAN': 'FCX',
    'GENERAL DYNAMICS': 'GD',
    'HERSHEY': 'HSY',
    'ALTRIA GROUP': 'MO',
    'AMERICAN TOWER': 'AMT',
    'CUMMINS': 'CMI',
    'DUKE ENERGY': 'DUK',
    'EQUINIX': 'EQIX',
    'EXELON': 'EXC',
    'HUMANA': 'HUM',
    'INTUIT': 'INTU',
    'KIMBERLY-CLARK': 'KMB',
    'KROGER': 'KR',
    'LOWE\'S': 'LOW',
    'MARATHON PETROLEUM': 'MPC',
    'NEXTERA ENERGY': 'NEE'
}


@bot.message_handler(commands=['start'])
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
 
bot.polling(none_stop=True)
