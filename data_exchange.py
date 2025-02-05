import requests
import pandas as pd
import os
from decouple import config

api_key=os.environ['ALPHA_VANTAGE_API_KEY'] = config('ALPHA_VANTAGE_API_KEY')
base_url = os.environ['BASE_URL'] = config('BASE_URL')


def get_data_collect(from_currency = 'USD', to_currency = 'EUR'):
            params = {
                'function': 'FX_DAILY',
                'from_symbol': from_currency,
                'to_symbol': to_currency,
                'apikey': api_key
            }
            response = requests.get(base_url, params=params)
            data = response.json()

            if 'Time Series FX (Daily)' in data:
                time_series = data['Time Series FX (Daily)']
                data = pd.DataFrame.from_dict(time_series, orient='index')
                data.columns = ['Open', 'High', 'Low', 'Close']
                data.index = pd.to_datetime(data.index)
                return data
            else:
                raise ValueError("Unexpected data format received from Alpha Vantage API")
        
def prepare_data(data):
        data['Close'] = pd.to_numeric(data['Close'])
        data['Date'] = data.index
        data = data[['Date', 'Close']]
        data['Date'] = data['Date'].map(lambda x: x.strftime('%Y-%m-%d'))
        return data.to_dict(orient='records')
        