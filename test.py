#!/usr/bin/env python

import cryptocompare
import datetime
import time

coins = ['BTC', 'ETH', 'ETC', 'XMR', 'DOGE', 'GNT', 'ZEC']
currencies = ['EUR', 'USD', 'GBP']

print('===================== PRICE ======================')
for coin in coins:
    print(cryptocompare.get_price(coin))
    print(cryptocompare.get_price(coin, curr='USD'))
    print(cryptocompare.get_price(coin, curr=['EUR','USD','GBP']))
    print(cryptocompare.get_price(coin, full=True))
    print(cryptocompare.get_price(coin, curr='USD', full=True))
    print(cryptocompare.get_price(coin, curr=['EUR','USD','GBP'], full=True))

print('==================================================')
print(cryptocompare.get_price(coins))
print(cryptocompare.get_price(coins, curr='USD'))
print(cryptocompare.get_price(coins, curr=['EUR','USD','GBP']))

print('==================== HIST PRICE ==================')
for coin in coins:
    print(cryptocompare.get_historical_price(coin))
    print(cryptocompare.get_historical_price(coin, curr='USD'))
    print(cryptocompare.get_historical_price(coin, curr=['EUR','USD','GBP']))
    print(cryptocompare.get_historical_price(coin, 'USD',datetime.datetime.now()))
    print(cryptocompare.get_historical_price(coin, ['EUR','USD','GBP'],time.time()))
