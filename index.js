//require('dotenv').config()
/*Executando código dentro do time out a cada instante determinado la no .env.
Pegamos esse instante usando "process.env.CRAWLER_INTERVAL".*/
const { parse } = require('dotenv');
const api = require('./api')

//Essa func deve ser assíncrona para esperar a resposta da func chamada antes do console.
setInterval(async() => {
    
    const result = await api.depth()
    console.log(`Maior ordem de compra atualmente: ${result.bids[0][0]}`)
    console.log(`Menor ordem de venda atualmente: ${result.asks[0][0]}`)

    const buy = parseInt(result.bids[0][0])
    const sell = parseInt(result.asks[0][0])

    if (sell<20000) console.log('Devemos comprar!')
    else if(buy>22000) console.log('Hora de vender!')
    else console.log('Esperando.')


}, process.env.CRAWLER_INTERNAL);

