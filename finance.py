import yfinance as yf
import time

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    try:
        data = stock.history(period="1d")
        return data['Close'].iloc[-1]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def monitor_stock_price(ticker, interval=10):
    while True:
        price = get_stock_price(ticker)
        if price is not None:
            print(f"Current {ticker} stock price: ${price:.2f}")
        time.sleep(interval)

if __name__ == "__main__":
<<<<<<< HEAD

   SYMBOL = 'SPY'  # Replace with the desired stock symbol

>>>>>>> origin/master
    monitor_stock_price(SYMBOL)
