import os
import ccxt

# API Keys (GitHub Secrets se uthata hai)
api_key = os.environ.get('DELTA_API_KEY')
secret_key = os.environ.get('DELTA_SECRET_KEY')

exchange = ccxt.delta({
    'apiKey': api_key,
    'secret': secret_key,
})

def execute_trade():
    symbol = 'ETH/USDT'
    amount = 1  # 1 contract
    leverage = 5    
    
    try:
        # Leverage set karna
        exchange.set_leverage(leverage, symbol)
        
        # BUY order place karna
        order = exchange.create_order(symbol, 'market', 'buy', amount)
        print("Trade Successful! Order Details:", order)
        
    except Exception as e:
        print("Error during trade:", e)

# Jab aap fully taiyar honge, tab main is function ko activate karunga.
# Filhal ke liye ye code bas connection test karega.
print("Bot script loaded successfully.")
