import CoinNode
import API
import time


def getCoinDict(): 
    #coinList = ['bitcoin', 'etherium', 'dogecoin', 'binancecoin', 'cardano', 'solana', 'ripple']
    coinList = ['bitcoin', 'eos', 'eth', 'link', 'usd', 'xrp', 'eur']
    #coinList = ['bitcoin', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'link', 'dot', 'yfi', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'gel', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'ngn', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau', 'bits', 'sats']
    coinDict : dict = {}


    for coin_from in coinList:

        #add each coin to dict
        coinDict[coin_from] = CoinNode.CoinNode(name=coin_from)
        print("getting edges from " + coin_from)

        #populate matrix
        for coin_to in coinList:
            if coin_from != coin_to:
                time.sleep(13)
                exchange_rate = API.get_crypto_exchange_rate(coin_from, coin_to)
                print(coin_from + " to " + coin_to + " is " + str(exchange_rate))
                if exchange_rate is not None:
                    coinDict[coin_from].exchangeRates[coin_to] = exchange_rate

    for coin in coinDict:
        print(coin + "->")
        print(coinDict[coin].exchangeRates)

    return coinDict



# testCoin = CoinNode(name = 'bitcoin')
# print(testCoin.name)

def getExchangeRate():
    # Example usage:
    crypto_from = 'bitcoin'
    crypto_to = 'eur'
    exchange_rate = API.get_crypto_exchange_rate(crypto_from, crypto_to)

    if exchange_rate is not None:
        print(f"The exchange rate from {crypto_from.upper()} to {crypto_to.upper()} is {exchange_rate}")
    else:
        print(f"Failed to retrieve the exchange rate")


#print(API.getValidCoinList())
getCoinDict()
#getExchangeRate()

