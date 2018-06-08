import numpy as np
import requests
import json

BASE_URL = 'https://api.iextrading.com/1.0'

def getPrice(sym):
    url = '{}/stock/{}/delayed-quote'.format(BASE_URL, sym)
    r = requests.get(url)
    data = json.loads(r.text)
    return(data["delayedPrice"])

def delayed_quote(sym):
    url = '{}/stock/{}/delayed-quote'.format(BASE_URL, sym)
    data = json.loads(requests.get(url).text)
    return data

def chart(sym, time='1d'):
    url = '{}/stock/{}/chart/{}'.format(BASE_URL, sym, time)
    data = json.loads(requests.get(url).text)
    return data

def financials(sym):
    url = '{}/stock/{}/financials'.format(BASE_URL, sym)
    data = json.loads(requests.get(url).text)
    return data

def stats(sym):
    url = '{}/stock/{}/stats'.format(BASE_URL, sym)
    data = json.loads(requests.get(url).text)
    return data
