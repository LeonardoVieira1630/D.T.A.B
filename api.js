//Contem as funções de comunicação com a api da binance


const axios = require('axios');
const crypto  = require('crypto');
const querystring = require('querystring');

const apiKey = process.env.API_KEY;
const apiSecret = process.env.SECRET_KEY
const apiUrl = process.env.API_URL

//Func para requisições privadas (compra, venda e afins)
async function privateCall(path, data = {}, method = 'GET'){

    //Para todas as chamadas é necessário passar o instante que ela foi gerada, logo:
    const timestamp = Date.now();
    //Usando a biblioteca crypto e o "gerador" de requisição HMAC, cripitografamos a requisição que vamos mandar
    const signature = crypto.createHmac('sha256', apiSecret)
                    .update(`${querystring.stringify({...data, timestamp})}`)
                    .digest('hex');

    const newData = {...data, timestamp , signature};
    const qs = `?${querystring.stringify(newData)}`

    try{
        const result = await axios({
            method,
            url: `${apiUrl}${path}${qs}`,
            headers: { 'X-MBX-APIKEY': apiKey}
        })
        return result.data
    }
    catch(err){
        console.log(err)
    }
}


async function accountInfo(){
    return privateCall('/v3/account');
}



//Func que faz requisição para a binance.
async function publicCall(path, data, method = 'GET'){

    try{
        //Essa const funciona como um if else.
        const qs = data ? `?${querystring.stringify(data)}` : '';
        const result = await axios({
            method,
            url: `${process.env.API_URL}${path}${qs}`
        })
        return result.data;
    }
    catch(err){
        //console.log(err)
    }
}


async function newOrder(symbol, quantity, price, side = 'BUY', type= 'MARKET'){
    const data = {symbol, side, type, quantity};

    if (price) data.price = price;
    if (type == 'LIMIT') data.timeInForce = 'GTC';

    return privateCall ('/v3/order', data, 'POST')
}


async function time(){
    return publicCall('/v3/time');
}

async function exchangeInfo(symbol) {
    const result = await publicCall('/v3/exchangeInfo');
    return symbol ? result.symbols.find(s => s.symbol === symbol) : result.symbols;
}

//Func que pede os dados do BTC.
async function depth(symbol = 'BTCBRL', limit =5){
    return publicCall('/v3/depth', {symbol, limit})
}

module.exports = {time, depth, exchangeInfo, accountInfo, newOrder}
