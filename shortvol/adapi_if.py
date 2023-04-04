import requests
import io
import pandas as pd

class ADAPIInterface():

    def __init__(self, API_KEY):
        self.headers = {
            "accept": "application/json",
            "x-api-key": API_KEY
        }


    def get_options_market_information(self, exchange="deribit", fmt="csv"):
        url = "https://web3api.io/api/v2/market/options/ohlcv/information"

        params = dict()
        params["exchange"] = exchange
        params["includeInactive"] = "false"
        params["timeFormat"] = "hr"
        params["format"] = fmt
    
        res = requests.get(url, headers=self.headers, params=params)

        if fmt == "csv":
            df = pd.read_csv(io.StringIO(res.text))
            return list(dict.fromkeys(list(df['underlying'])))