#!/usr/bin/env python3

# import sys, os
# sys.path.insert(0, os.path.abspath('..'))

import unittest
import cryptocompare



class TestCryptoCompare(unittest.TestCase):
  def assertCoinAndCurrInPrice(self, coin, curr, price):
    if isinstance(coin, list):
      for co in coin:
        self.assertCoinAndCurrInPrice(co, curr, price)
      return
    else:
      self.assertIn(coin, price)

    if isinstance(curr, list):
      for cu in curr:
        self.assertIn(cu, price[coin])
    else:
      self.assertIn(curr, price[coin])

  def test_coin_list(self):
    lst = cryptocompare.get_coin_list()
    self.assertTrue('BTC' in lst.keys())
    lst = cryptocompare.get_coin_list(True)
    self.assertTrue('BTC' in lst)

  def test_get_price(self):
    coin = 'BTC'
    price = cryptocompare.get_price(coin)
    self.assertCoinAndCurrInPrice(coin, 'EUR', price)
    price = cryptocompare.get_price(coin, curr='USD')
    self.assertCoinAndCurrInPrice(coin, 'USD', price)
    currencies = ['EUR','USD','GBP']
    price = cryptocompare.get_price(coin, curr=currencies)
    self.assertCoinAndCurrInPrice(coin, currencies, price)
    coins = ['BTC', 'XMR']
    price = cryptocompare.get_price(coins, curr=currencies)
    self.assertCoinAndCurrInPrice(coins, currencies, price)

  def test_get_price_full(self):
    price = cryptocompare.get_price('ETH', full=True)
    self.assertIn('RAW', price)
    self.assertIn('ETH', price['RAW'])
    self.assertIn('EUR', price['RAW']['ETH'])
    self.assertIn('PRICE', price['RAW']['ETH']['EUR'])


if __name__ == "__main__":
  unittest.main()