#!/usr/bin/python3.8
import requests
import csv
import datetime
import pymongo
import time
import os
import logging

def download(url):
    response = requests.get(url)
    if response:
        return response.text

if __name__ == '__main__':
    while True:
        try:
            server = pymongo.MongoClient(f"mongodb://{os.environ['mongodb-server']}:27017/")
            db = server['orderbook']
            
            xrp = download('https://api.bittrex.com/v3/markets/XRP-USDT/orderbook')
            btc = download('https://api.bittrex.com/v3/markets/BTC-USDT/orderbook')
            eth = download('https://api.bittrex.com/v3/markets/ETH-USDT/orderbook')
            ltc = download('https://api.bittrex.com/v3/markets/LTC-USDT/orderbook')
            eos = download('https://api.bittrex.com/v3/markets/EOS-USDT/orderbook')

            date = datetime.datetime.now()

            db['xrp'].insert_one({'date': date, 'orderbook': xrp})
            db['btc'].insert_one({'date': date, 'orderbook': btc})
            db['eth'].insert_one({'date': date, 'orderbook': eth})
            db['ltc'].insert_one({'date': date, 'orderbook': ltc})
            db['eos'].insert_one({'date': date, 'orderbook': eos})

            logging.info('completed iter')
        except Exception as ex:
            print(f'Issues: {ex}')
        
        time.sleep(60)



    

