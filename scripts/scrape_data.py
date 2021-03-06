import requests, pickle, time, sys

from datetime import datetime
from multiprocessing import Process

class DataScraper():
    def __init__(self,root,tickers,delay,market_close):
        self.root = root
        self.tickers = tickers
        self.delay = delay
        self.market_close = market_close

        self.procs = []
        self.keys = ["bidPrice", "askPrice", "bidSize", "askSize", "lastSalePrice", "lastSaleSize"]

    def ds_run(self):
        for ticker in self.tickers:
            proc = Process(target = self.scrape_iex,args=(ticker,))
            self.procs.append(proc)
            proc.start()
        for proc in self.procs:
            proc.join()

    def scrape_iex(self,ticker):
        data = {}
        for k in self.keys:
            data[k] = []
        data["time"] = []
        data["ticker"] = ticker

        while datetime.now().hour < self.market_close:
            req = requests.get("https://api.iextrading.com/1.0/tops?symbols=" + ticker)
            req2 = req.json()[0]
            for k in self.keys:
                data[k].append(req2[k])
            data["time"].append(time.time())

            if datetime.now().minute == 0 or datetime.now().minute == 10 or datetime.now().minute == 20 or datetime.now().minute == 30 or datetime.now().minute == 40 or datetime.now().minute == 50:
                try:
                    with(open("%s/data/checkpoints/%s_data_checkpoint.pkl" % (self.root,ticker),"wb")) as f:
                        pickle.dump(data,f)
                except:
                    print(str(time.time()) + " | COULD NOT SAVE CHECKPOINT")
            time.sleep(self.delay)

        with(open("%s/data/checkpoints/%s_data_checkpoint.pkl" % (self.root, ticker), "wb")) as f:
            pickle.dump(data, f)
