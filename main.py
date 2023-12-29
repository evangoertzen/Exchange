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
        #print("Populating exchange rates for ", coin_from)

        #populate matrix
        for coin_to in coinList:
            if coin_from != coin_to:
                time.sleep(13)
                exchange_rate = API.get_crypto_exchange_rate(coin_from, coin_to)
                #print(coin_from + " to " + coin_to + " is " + str(exchange_rate))
                if exchange_rate is not None:
                    coinDict[coin_from].exchangeRates[coin_to] = exchange_rate

        print(coin_from, "-> ", coinDict[coin_from].exchangeRates)

    return coinDict

def getExchangeRate():
    crypto_from = 'bitcoin'
    crypto_to = 'eur'
    exchange_rate = API.get_crypto_exchange_rate(crypto_from, crypto_to)

    if exchange_rate is not None:
        print(f"The exchange rate from {crypto_from.upper()} to {crypto_to.upper()} is {exchange_rate}")
    else:
        print(f"Failed to retrieve the exchange rate")


def dfs(coinDict, start, visited, path, path_product):
    #print("dfs at " + start + ", path_product = ", path_product)
    visited[start] = True
    path.append(start)

    for neighbor in coinDict[start].exchangeRates:
        if not visited[neighbor]:
            if dfs(coinDict, neighbor, visited, path, path_product*coinDict[start].exchangeRates[neighbor]):
                return True
            
        elif path_product*coinDict[start].exchangeRates[neighbor] > 1:
            #cycle detected
            cycle_start_index = path.index(neighbor)
            cycle = path[cycle_start_index:]
            print("Cycle: ", cycle)
            print("Val: ", path_product*coinDict[start].exchangeRates[neighbor])
            return True
        
    path.pop()
    visited[start] = False
    return False


def findPositiveCycles(coinDict):
    visited : dict = {}
    for coin in coinDict:
        visited[coin] = False

    for coin in coinDict:
        if not visited[coin]:
            path = []
            if dfs(coinDict, coin, visited, path, 1):
                return True

    return False


def createSampleCoinDict():

    #add nodes to dict
    coinDict : dict = {}
    coinDict['A'] = CoinNode.CoinNode(name='A')
    coinDict['B'] = CoinNode.CoinNode(name='B')
    coinDict['C'] = CoinNode.CoinNode(name='C')
    coinDict['D'] = CoinNode.CoinNode(name='D')

    #add edges
    coinDict['A'].exchangeRates['B'] = 2.0
    coinDict['A'].exchangeRates['D'] = 1.0
    coinDict['B'].exchangeRates['D'] = 1.0
    coinDict['D'].exchangeRates['C'] = 0.5
    coinDict['C'].exchangeRates['B'] = 1.5

    return coinDict

def testDfs():
    Visited : dict = {}
    Visited['A'] = False
    Visited['B'] = False
    Visited['C'] = False
    Visited['D'] = False
    if dfs(createSampleCoinDict(), 'A', Visited, [], 1):
        print("found cycle")
    else:
        print("didn't find cycle")


#getCoinDict()
#getExchangeRate()

#testDfs()
findPositiveCycles(getCoinDict())
