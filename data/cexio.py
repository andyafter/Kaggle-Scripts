import urllib2, cookielib


ticker = "https://cex.io/api/ticker/BTC/USD"


class TickerData(object):
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        self.all_pairs = "https://cex.io/api/tickers/USD/EUR/RUB/BTC"

    def tick(self):
        req_all = urllib2.Request(self.all_pairs, headers=self.header)
        all_tick = urllib2.urlopen(req_all)
        all_tick_data = all_tick.read()
        return all_tick_data

    def wss_tick(self):
        return []
