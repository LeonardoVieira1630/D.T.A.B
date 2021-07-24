//require('dotenv').config()
/*Executando código dentro do time out a cada instante determinado la no .env.
Pegamos esse instante usando "process.env.CRAWLER_INTERVAL".*/
//const { parse } = require('dotenv');
const api = require('./api')
const symbol = process.env.SYMBOL
const profitability = process.env.PROFITABILITY
const coin = process.env.COIN


console.log('Iniciando monitoramento!');


//Essa func deve ser assíncrona para esperar a resposta da func chamada antes do console.
setInterval(async() => {

    console.log(`Mercado para ${symbol}`);
    let sell=0, buy=0;
    const result = await api.depth(symbol)
    if(result.bids && result.bids.length){
        console.log(`Maior ordem de compra atualmente: ${result.bids[0][0]}`)
        buy = parseFloat(result.bids[0][0])
    }
    if(result.asks && result.asks.length){
        console.log(`Menor ordem de venda atualmente: ${result.asks[0][0]}`)
        sell = parseFloat(result.asks[0][0])
    }

    // alterar esse valor para um valor condizente 
    if (sell && sell<700) {
        console.log('Devemos comprar!')
        const account = await api.accountInfo();
        const coins = account.balances.filter(b => symbol.indexOf(b.asset) !== -1)
        console.log('Posição da carteira: ')
        console.log(coins);

        //Para outras moedas (btc), revisar essa parte no 2 - 8
        console.log('Verificando se tenho dinheiro...')

        const carteiraUSD = parseFloat(coins.find(c => c.asset.endsWith(coin)).free);
        //Da pra melhorar essa precisão com base na moeda que vamos usar.
        const qty = parseFloat((carteiraUSD/sell) - 0.00001).toFixed(5);
        console.log(qty)
        
        if(sell <= qty){

            console.log('Tenho! Comprando!');
            const buyOrder = await api.newOrder(symbol, qty);
            console.log(`orderId: ${buyOrder.orderId}`);
            console.log(`status: ${buyOrder.status}`);

            if(buyOrder === 'FILLED'){
                const price = parseFloat(sell * profitability).toFixed(5);
                console.log(`Posicionando venda. Ganho de ${profitability}`);
                console.log('Vendendo por: ' + price)
                const sellOrder = await api.newOrder(symbol, 1,  price, 'SELL', 'LIMIT');
                console.log(`orderId: ${sellOrder.orderId}`);
                console.log(`status: ${sellOrder.status}`);
            }

            else{
                console.log('Compra não efetuada com sucesso.')
            }

        }
        
    }
    else if(buy && buy>1000) console.log('Hora de vender!') 
    // esse elseif é pra se eu quiser implementar
    //alguma lógica de venda (atualmente estou colocando a 
    //venda em 10% do preço que comprei).
    else console.log('Esperando.')
    
   //console.log(await api.exchangeInfo())

}, process.env.CRAWLER_INTERNAL);

