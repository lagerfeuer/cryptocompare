#!/usr/bin/env python3

import unittest
import cryptocompare
import datetime


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
    currencies = ['EUR', 'USD', 'GBP']
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

  def test_get_historical_price(self):
    coin = 'XMR'
    curr = 'EUR'
    price = cryptocompare.get_historical_price(
        'XMR', timestamp=datetime.datetime(2017, 6, 6), exchange='CCCAGG')
    self.assertCoinAndCurrInPrice(coin, curr, price)
    price2 = cryptocompare.get_historical_price(
        'XMR', 'EUR', datetime.datetime(2017, 6, 6))
    self.assertCoinAndCurrInPrice(coin, curr, price2)
    self.assertEqual(price, price2)

  def test_price_day(self):
    coin = 'BTC'
    curr = 'USD'
    price = cryptocompare.get_historical_price_day(coin, curr=curr, limit=3)
    for frame in price:
      self.assertIn('time', frame)

  def test_price_hour(self):
    coin = 'BTC'
    curr = 'USD'
    price = cryptocompare.get_historical_price_hour(coin, curr=curr, limit=3)
    for frame in price:
      self.assertIn('time', frame)

  def test_price_minute(self):
    coin = 'BTC'
    curr = 'USD'
    price = cryptocompare.get_historical_price_minute(coin, curr=curr, limit=3)
    for frame in price:
      self.assertIn('time', frame)

  def test_get_avg(self):
    coin = 'BTC'
    curr = 'USD'
    avg = cryptocompare.get_avg(coin, curr, exchange='Kraken')
    self.assertEqual(avg['LASTMARKET'], 'Kraken')
    self.assertEqual(avg['FROMSYMBOL'], coin)
    self.assertEqual(avg['TOSYMBOL'], curr)

  def test_get_exchanges(self):
    exchanges = cryptocompare.get_exchanges()
    self.assertIn('Kraken', exchanges)


if __name__ == "__main__":
  unittest.main()
