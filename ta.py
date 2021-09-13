import numpy, talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv', delimiter=',')
close = my_data[:,4]
print(close)



moving_avarage = talib.SMA(close,timeperiod = 2)



rsi = talib.RSI(close)

print(rsi)
