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



class Stock_Info:

    
    def __init__(self, symbol):
        
        # takes a symbol that's entered in:
        self.stock_symbol = symbol.replace(' ', '')
        
        # url used to try and find the stock that's needed:
        self.url = ureq.urlopen("https://finance.yahoo.com/quote/" + self.stock_symbol + "?p=" + self.stock_symbol).read()

        # beautiful soup shit:
        self.soup = BeautifulSoup(self.url, "html.parser")
        self.title = self.soup.find_all('h1')[0]
        self.stock_data = {
            "Stock_Symbol": self.__find_symbol_title__()['Stock_Symbol'],
            "Stock_Name": self.__find_symbol_title__()['Stock_Name'],
            "stock_price": float(self.soup.find_all('span')[27].text.replace(',','')),
            "stock_change_amount": self.__fix_stock_change__()[0],
            "stock_change_percent": self.__fix_stock_change__()[1],
        }

    def __find_symbol_title__(self):

        symbol_len = len(self.title.text.split(' '))
        symbol = self.title.text.split(' ')[symbol_len - 1]
        symbol_len = len(symbol)
        symbol = list(symbol)
        symbol.pop(0)
        symbol.pop(symbol_len - 2)    
        symbol = ''.join(symbol)


        name = self.title.text
        name = name.split(' ')
        name_len = len(name)
        name.pop(name_len - 1)
        name = ' '.join(name)


        return ({
            "Stock_Symbol": symbol,
            "Stock_Name": name
        })
        
    def __fix_stock_change__(self):
        change = self.soup.find_all('span')[28].text
        change = change.split(" ")
        change_amt = float(change[0])
        change_per = list(change[1])
        change_per_len = len(change_per)
        change_per.pop(0)
        change_per.pop(change_per_len - 2)    
        change_per.pop(change_per_len - 3)    
        change_per = float(''.join(change_per))

        return [
            change_amt,
            change_per
        ]
        

while True:
    print("what stock are you looking for?")
    stock_symbol = input()
    x = Stock_Info(y)
    print(x.stock_data)