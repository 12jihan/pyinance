# how to find the stock you're looking for:
# https://finance.yahoo.com/quote/msft?p=msft

from bs4 import BeautifulSoup

import urllib.request as ureq
import urllib.parse as uparse
import urllib.error as uerror

import json
import re

import pymongo