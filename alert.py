import ccxt
import pandas_ta as ta
import pandas as pd
import requests

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

last_row = df.iloc[-1]

print(last_row)

WEBHOOK_URL = "https://discord.com/api/webhooks/914592512541335634/s33NsAq6d7kUbNGbRMm2dGLuaHTtLEHDjJK4T1JRdAkuBN3-VI4kxmPM0Dk_yXsmN1jO"


if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: The ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMP_14'] < last_row['DMN_14']:
        message = f"STRONG DOWNTREND: The ADX is {last_row['ADX_14']:.2f}"

    print(message)

    payload = {
        "username": "alertbot",
        "content": message
    }

    requests.post(WEBHOOK_URL, json=payload)


if last_row['ADX_14'] < 25:
    message = f"NO TREND: The ADX is {last_row['ADX_14']:.2f}"

    print(message)

    payload = {
        "username": "alertbot",
        "content": message
    }

    requests.post(WEBHOOK_URL, json=payload)
