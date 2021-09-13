import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.SECRET_KEY, testnet=True)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

csvfile = open('novo.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "7 Sep, 2021")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Jul, 2020")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000.0
    candlestick_writer.writerow(candlestick)

csvfile.close()
