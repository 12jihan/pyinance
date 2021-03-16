from bs4 import BeautifulSoup
import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror

import json
import re
import time
import uuid

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pyinance']
collection = db['stocks']

print("collection info: \n", collection)


info = dir(collection)

for x in info:
    print("\n" + x)
# print(db.collection_names())

def most_active_stocks():
    # Goes to yahoo finances
    x = ureq.urlopen("https://finance.yahoo.com/most-active").read()
    soup = BeautifulSoup(x, "html.parser")

    for x in range(1, 26):
        data0 = soup.find_all("tr")[x]
        data1 = list(data0.children)

        stock_info = {
            "_id": str(uuid.uuid4()),
            "symbol": data1[0].text,
            "name": data1[1].text,
            "price": float(data1[2].text),
            "change": float(data1[3].text),
            "per_change": data1[4].text,
            "volume": data1[5].text,
            "avg_volume": data1[6].text,
            "market_cap": data1[7].text,
            "pe_ratio": data1[8].text,
            "last_update": int(time.time())
        }

        print(stock_info)
        collection.insert_one(stock_info)
        print('inserted: ', stock_info['symbol'])

most_active_stocks()
