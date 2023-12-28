import requests

def get_crypto_exchange_rate(from_currency, to_currency):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data and to_currency in data[from_currency]:
            return data[from_currency.lower()][to_currency.lower()]
        else:
            return None
    else:
        return None
    
def getExchangeMatrix():
    url = 'https://api.coingecko.com/api/v3/simple/matrix'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def getValidCoinList():
    url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        #coin_names = [coin['id'] for coin in data]
        return data
    else:
        return None
