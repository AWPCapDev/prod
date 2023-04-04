class ORouter():
    
    def __init__(self, exchange_name, api_key, useFixApi=False):
        self.exchange_name = exchange_name
        self.api_key = api_key
        self.exchanges = [
            'deribit',
            'cme'
            'lme'
        ]
        self.useFixApi = useFixApi

    def parseOrder(self, ticker):
        """
            BTC-28APR23-28000-P
        """
        S, T, K, _d = ticker.split('-')
        return {
            'underlying': S,
            'tte': T,
            'strike': K,
            'cp': _d
        }

    def sendOrder():
        pass

    def logOrder():
        pass

    def sendOrderToPost():
        pass