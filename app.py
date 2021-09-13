"""
    app.py cuida, por meio do flask, a gerenciar a interface web, ou seja,
Aqui passaremos as informações de cada endpoint.
"""

#Importações
from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv, datetime
from binance.client import Client
from binance.enums import *
from flask_cors import CORS


#Criando nosso app com o flask
app = Flask(__name__)
CORS(app)
app.secret_key = b'somelongrandomstring'


#Para usar a conta real teremos que tirar a parte do teste net e mudar as keys
client = Client(config.API_KEY,config.SECRET_KEY, testnet=True)


#Principal end-point. 
@app.route('/')
def index():
    title = 'D.T.A.B'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index2.html', title=title, my_balances=balances, symbols=symbols)


#Quando ordenarmos uma compra:
@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_order(symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')


#Quando ordenarmos uma compra:
@app.route('/sell')
def sell():
    return 'sell'


#Se houver mudança nas settings do rsi:
@app.route('/settings')
def settings():
    return 'settings'


#End-point para as informações do grafico.
@app.route('/history')
def history():
    candlesticks = client.get_historical_klines_generator("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "6 Sep, 2021")

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000, 
            "open": data[1],
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }
        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)