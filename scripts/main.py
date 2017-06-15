from argparse import ArgumentParser
from configparser import ConfigParser

import os, sqlite3

if __name__ == '__main__':
    root = os.path.realpath(__file__)[:-7]

    cfg = ConfigParser()
    cfg.read(root + "/cfg/cfg.ini")

    tickers = cfg["scraper"]["tickers"].split(",")
    delay = int(cfg["scraper"]["delay"])
    market_close = int(cfg["general"]["market_close"])

    parser = ArgumentParser()
    parser.add_argument("module")
    args = parser.parse_args()

    if args.module == "pre":
        from scripts.pre_market import *
        sess = PreMarket(root)
        sess.pre_run()
    elif args.module == "post":
        from scripts.post_market import *
        conn = sqlite3.connect(root + "/data/l2.db")
        cursor = conn.cursor()
        sess = PostMarket(root,conn,cursor)
        sess.post_run()
    elif args.module == "scrape" or args.module == "scraper":
        from scripts.scrape_data import *
        sess = DataScraper(root,tickers,delay,market_close)
        sess.ds_run()