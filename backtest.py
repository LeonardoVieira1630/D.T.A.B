"""
    O backtest.pt roda uma simulação de como a estratégia do rsi performaria em
um determinado periodo de tempo.
    Essa biblioteca é fenomenal para testes antes de realmente colocarmos
dinheiro na aplicação. 
"""

#Importação
import backtrader as bt

#Criando a classe da nossa estratégia
class RSIStrategy(bt.Strategy):

    def __init__(self):
       self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=0.1)#Quantidade da moeda
        
        if self.rsi > 70 and self.position:
            self.close()



cerebro = bt.Cerebro()

#data = bt.feeds.GenericCSVData(dataname='daily.csv',dtformat = 2)
data = bt.feeds.GenericCSVData(dataname='novo.csv',dtformat = 2,timeframe=bt.TimeFrame.Minutes,compression=15)

cerebro.adddata(data)
cerebro.addstrategy(RSIStrategy)

cerebro.run()
cerebro.plot()

