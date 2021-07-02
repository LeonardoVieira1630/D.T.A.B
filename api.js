//Contem as funções de comunicação com a api da binance

const axios = require("axios")
const querystring = require('querystring')


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
        console.log(err)
    }
}

/*
async function time(){
    return publicCall('/v3/time');
}
*/

//Func que pede os dados do BTC.
async function depth(symbol = 'BTCBRL', limit =5){
    return publicCall('/v3/depth', {symbol, limit})
}

module.exports = {depth}
