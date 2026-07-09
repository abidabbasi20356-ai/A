import os
import ccxt

api_key = os.environ.get('DELTA_API_KEY')
secret_key = os.environ.get('DELTA_SECRET_KEY')

exchange = ccxt.delta({
    'apiKey': api_key,
    'secret': secret_key,
    'enableRateLimit': True,
})


def run_bot():
    symbol = 'ETH/USDT'
    amount = 1 
    leverage = 5
    
    # Leverage set karna
    exchange.set_leverage(leverage, symbol)
    
    # 1. Market Data fetch karna
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='15m', limit=21)
    closes = [candle[4] for candle in ohlcv]
    volumes = [candle[5] for candle in ohlcv]
    
    sma = sum(closes[-20:]) / 20
    avg_vol = sum(volumes[-20:20]) / 20
    
    # 2. Strategy Logic (Volume Breakout)
    if closes[-1] > sma and volumes[-1] > (avg_vol * 1.5):
        print("Breakout Detected: Buying...")
        # BUY Order
        order = exchange.create_order(symbol, 'market', 'buy', amount)
        print("Trade Placed:", order)
        
    # 3. Trailing/Exit Logic (0.5% Profit/Loss management)
    # Delta Exchange par trailing ke liye 'trailing_stop' order use hota hai
    params = {'trailing_stop_activation_price_offset': 0.5, 'trailing_stop_callback_rate': 0.5}
    # Yahan hum stop-loss ya exit trigger kar sakte hain agar zaroorat ho

run_bot()
        
