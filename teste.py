import requests
import pandas as pd

# Configurações da API Alpha Vantage
API_KEY = 'alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

def get_exchange_rate_data(from_currency='USD', to_currency='EUR'):
    params = {
        'function': 'FX_DAILY',
        'from_symbol': from_currency,
        'to_symbol': to_currency,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Verifica se a chave 'Time Series FX (Daily)' está presente nos dados retornados
    if 'Time Series FX (Daily)' in data:
        time_series = data['Time Series FX (Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.columns = ['Open', 'High', 'Low', 'Close']
        df.index = pd.to_datetime(df.index)
        return df
    else:
        raise ValueError("Unexpected data format received from Alpha Vantage API")

# Exemplo de uso
try:
    df = get_exchange_rate_data()
    print(df.head())
except ValueError as e:
    print(e)
