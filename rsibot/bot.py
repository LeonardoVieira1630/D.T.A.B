"""
    O código bot.py roda e fica recebendo as informações da moeda escolhia.
Quando Recebe informação de fechamento do candle, ele armazena em um array
que quando atinge tamanho de 10, começa a calcular o rsi. Dependendo das
condições do indicador, a operação de compra e venda é feita automaticamente.
"""


#Importações
import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *


#Constantes
SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_5m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSDT'
TRADE_QUANTITY = 0.001


#Armazenda os preços de candles
closes = []
#Diz se o candle fechou ou não
in_position = False


#client = Client(config.API_KEY, config.API_SECRET, tld='us')

#O cliente diz com quem vamos fazer as comunicaçoes de compra e 
#requisição de dados.
client = Client(config.API_KEY,config.SECRET_KEY, testnet=True)


#Função geral para passar uma ordem de compra ou venda para a corretora
def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True


#Necessarias para comunicar com a Binance
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')


#Função que lida com a estratégia do rsi e com o controle dos dados
def on_message(ws, message):
    global closes, in_position
    
    #Recebendo dados de candle da binance
    print('received message')
    json_message = json.loads(message)
    #pprint.pprint(json_message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']
    pprint.pprint(candle)


    #Caso a mensagem recebida contiver o valor final do candle, entramos aqui
    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close)) #Adicionando a informação ao array
        print("closes")
        print(closes)


        #Se ja tivermos informações suficientes para o calculo:
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))


            #Caso o indicador mostre que o mercado esta sobre-comprado, vendemos.
            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! Sell! Sell! Sell!")
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")
            

            #Caso o indicador mostre que o mercado esta sobre-vendido, vendemos.
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversold! Buy! Buy! Buy!")
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True


#Conexão via websocket com a Binance       
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()