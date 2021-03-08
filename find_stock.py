# how to find the stock you're looking for:
# https://finance.yahoo.com/quote/msft?p=msft

from bs4 import BeautifulSoup

import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror

import json
import re

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pyinance']
collection = db['most-active']
stock = "plug"

x = ureq.urlopen("https://finance.yahoo.com/quote/" + stock + "?p=" + stock).read()
soup = BeautifulSoup(x, "html.parser")
title = soup.find_all('h1')[0]
data = {
    "stock_price": soup.find_all('span')[27],
    "stock_change": soup.find_all('span')[28],
}


# num = 0
# for x in title:
    # symbol_len = len(x.text.split(' '))
    # symbol = x.text.split(' ')[symbol_len - 1]
    # symbol_len = len(symbol)
    # symbol = list(symbol)
    # symbol.pop(0)
    # symbol.pop(symbol_len - 2)    
    # symbol = ''.join(symbol)

    # name = x
    # name = x.split(" ")
    # name_len = len(name)
    # name.pop(name_len - 1)
    # name = ' '.join(name)

    # print("------------------------")
    # print(name)
    # print(num)
    # num += 1 
# cycling through every span to find what i need and marking it:
# for x in data:
#     print("---------------")
#     print(x)
#     print(num)
#     num += 1


def find_symbol_title(x):

    symbol_len = len(x.text.split(' '))
    symbol = x.text.split(' ')[symbol_len - 1]
    symbol_len = len(symbol)
    symbol = list(symbol)
    symbol.pop(0)
    symbol.pop(symbol_len - 2)    
    symbol = ''.join(symbol)


    name = x.text
    name = name.split(' ')
    name_len = len(name)
    name.pop(name_len - 1)
    name = ' '.join(name)

    print({
        "Stock_Symbol": symbol,
        "Stock_Name": name
    })
    return ({
        "Stock_Symbol": symbol,
        "Stock_Name": name
    })

find_symbol_title(title)