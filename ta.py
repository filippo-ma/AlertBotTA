import ccxt
import pandas_ta as ta
import pandas as pd


exchange = ccxt.ftx()


bars = exchange.fetch_ohlcv('SOL/USD', timeframe='5m', limit=500)


df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])


adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

# obv = df.ta.obv()
# ad = df.ta.ad()
# aroon = df.ta.aroon()
# stoch = df.ta.stoch()


df = pd.concat([df, adx, macd, rsi], axis=1)



print(df)










