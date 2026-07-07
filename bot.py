import os
import ccxt

# GitHub Secrets se keys lena
api_key = os.environ.get('DELTA_API_KEY')
secret_key = os.environ.get('DELTA_SECRET_KEY')

# Delta Exchange se connect karna
exchange = ccxt.delta({
    'apiKey': api_key,
    'secret': secret_key,
})

# Balance check karke test karna
try:
    balance = exchange.fetch_balance()
    print("Connection successful! Aapka balance:", balance['total']['USDT'])
except Exception as e:
    print("Error:", e)
  
