#!/usr/bin/env python

import cryptocompare
import datetime
import time
import unittest

coins = ['BTC', 'ETH', 'XMR', 'NEO']
currencies = ['EUR', 'USD', 'GBP']


class TestCryptoCompare(unittest.TestCase):

    # cryptocompare.get_coin_list
    def test_get_coin_list(self):
        res = cryptocompare.get_coin_list()
        self.assertTrue(len(res) > 0, "expected data")
        self.assertEqual(res['ETH']['CoinName'], 'Ethereum')

    # cryptocompare.get_rate_limit_*
    def test_get_rate_limit_all(self):
        res = cryptocompare.get_rate_limit_all()
        self.assertTrue(res['Hour']['CallsLeft']['Histo'] > 0, "It have not hit hourly historical data calls limit")
        self.assertTrue(res['Minute']['CallsLeft']['Histo'] > 0, "It have not hit per minute historical data calls limit")

    def test_get_rate_limit_minute(self):
        res = cryptocompare.get_rate_limit_minute()
        self.assertTrue(res['CallsLeft']['Histo'] > 0, "It have not hit per minute historical data calls limit")

    # cryptocompare.get_exchanges
    def test_get_exchanges(self):
        res = cryptocompare.get_exchanges()
        self.assertIsNotNone(res['CCCAGG'])
        self.assertIsNotNone(res['Binance']['BTC'])

    # cryptocompare.get_historical_price
    def test_get_historical_price(self):
        res = cryptocompare.get_historical_price(coins[0])
        self.assertTrue(coins[0] in res.keys(), "expected coin requested data")
        self.assertTrue(res[coins[0]]['USD'] > 0, "Obtained a price and it is bigger than 0")  # USD is default currency

    def test_get_historical_price_against_currency(self):
        res = cryptocompare.get_historical_price(coins[0], currency='EUR')
        self.assertTrue(coins[0] in res.keys(), "expected coin requested data")
        self.assertFalse(coins[1] in res.keys(), "We do not expect data from non requested coin")
        self.assertTrue(res[coins[0]]['EUR'] > 0, "Obtained a price and it is bigger than 0")

    def test_get_historical_price_giving_timestamp(self):
        res = cryptocompare.get_historical_price(coins[1],currency='EUR',
                                                 timestamp= datetime.datetime.now() - datetime.timedelta(days=1, hours=-5))
        self.assertTrue(coins[1] in res.keys(), "expected coin requested data")
        self.assertFalse(coins[0] in res.keys(), "We do not expect data from non requested coin")
        self.assertTrue(res[coins[1]]['EUR'] > 0, "Obtained a price and it is bigger than 0") # This doesn't prove the price is right

    def test_get_historical_price_against_currency(self):
        res = cryptocompare.get_historical_price(coins[0], currency='EUR', exchange='Kraken')
        self.assertTrue(coins[0] in res.keys(), "expected coin requested data")
        self.assertTrue(res[coins[0]]['EUR'] > 0, "Obtained a price and it is bigger than 0")

    # cryptocompare.get_historical_price_day
    def test_get_historical_price_day(self):
        res = cryptocompare.get_historical_price_day(coins[0])
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(31, len(res['Data']), "response data limit defaults to 31 days")

    def test_get_historical_price_day_custom_limit(self):
        res = cryptocompare.get_historical_price_day(coins[0], limit=90)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(91, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_day_non_default_currency(self):
        res = cryptocompare.get_historical_price_day(coins[0], currency='USD', limit=10)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(11, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_day_from_exchange(self):
        res = cryptocompare.get_historical_price_day('ETH', currency='BTC', exchange='Cryptopia')
        self.assertTrue('Data' in res.keys(), "expected 'Data'")

    # cryptocompare.get_historical_price_hour
    def test_get_historical_price_hour(self):
        res = cryptocompare.get_historical_price_hour(coins[2])
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(25, len(res['Data']), "response data limit defaults to 31 days")

    def test_get_historical_price_hour_custom_limit(self):
        res = cryptocompare.get_historical_price_hour(coins[1], limit=90)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(91, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_hour_non_default_currency(self):
        res = cryptocompare.get_historical_price_hour(coins[0], currency='USD', limit=10)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(11, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_hour_from_exchange(self):
        res = cryptocompare.get_historical_price_hour('ETH', currency='BTC', exchange='Cryptopia')
        self.assertTrue('Data' in res.keys(), "expected 'Data'")

    # cryptocompare.get_historical_price_minute
    def test_get_historical_price_minute(self):
        res = cryptocompare.get_historical_price_minute(coins[0])
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(31, len(res['Data']), "response data limit defaults to 31 days")

    def test_get_historical_price_minute_custom_limit(self):
        res = cryptocompare.get_historical_price_minute(coins[2], limit=90)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(91, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_minute_non_default_currency(self):
        res = cryptocompare.get_historical_price_minute(coins[1], currency='USD', limit=10)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")
        # XXX: cryptocompare is off-by-one
        self.assertEqual(11, len(res['Data']), "expected limit to match days returned, got {}".format(len(res['Data'])))

    def test_get_historical_price_minute_from_exchange_and_aggregation(self):
        res = cryptocompare.get_historical_price_minute('ETH', currency='BTC', exchange='Cryptopia', aggregate=5)
        self.assertTrue('Data' in res.keys(), "expected 'Data'")

    def test_daily_avg(self):
        res = cryptocompare.get_historical_price(coins[0], currency='EUR')
        self.assertTrue(coins[0] in res.keys(), "expected coin requested data")
        self.assertFalse(coins[1] in res.keys(), "We do not expect data from non requested coin")
        self.assertTrue(res[coins[0]]['EUR'] > 0, "Obtained a price and it is bigger than 0")

    # cryptocompare.get_avg
    def test_get_avg(self):
        res = cryptocompare.get_avg(coins[1])
        self.assertTrue(len(res) > 0)
        self.assertTrue(float(res['PRICE']) > 0)

    def test_get_avg_given_exchange(self):
        res = cryptocompare.get_avg(coins[0], exchange='Kraken')
        self.assertTrue(len(res) > 0)
        self.assertTrue(float(res['PRICE']) > 0)

    # cryptocompare.get_price
    def test_get_price_defaults(self):
        res=cryptocompare.get_price('BTC')
        self.assertIsNotNone(res[coins[0]])
        self.assertTrue(float(res[coins[0]][cryptocompare.DEFAULT_CURRENCY]) > 0)

    def test_get_price_against_currency(self):
        res=cryptocompare.get_price(coins[0], currencies=currencies[0])
        self.assertIsNotNone(res[coins[0]])
        self.assertIsNotNone(res[coins[0]][currencies[0]])
        self.assertTrue(float(res[coins[0]][currencies[0]]) > 0)

    def test_get_price_multiple_coins(self):
        res=cryptocompare.get_price(coins[0:2], currencies=currencies[0])
        self.assertIsNotNone(res[coins[0]])
        self.assertIsNotNone(res[coins[1]])
        self.assertIsNotNone(res[coins[0]][currencies[0]])
        self.assertIsNotNone(res[coins[1]][currencies[0]])
        self.assertTrue(float(res[coins[0]][currencies[0]]) > 0)
        self.assertTrue(float(res[coins[1]][currencies[0]]) > 0)

    def test_get_price_multiple_currencies(self):
        res = cryptocompare.get_price(coins[0], currencies=currencies[0:2])
        self.assertIsNotNone(res[coins[0]])
        self.assertIsNotNone(res[coins[0]][currencies[0]])
        self.assertIsNotNone(res[coins[0]][currencies[1]])
        self.assertTrue(float(res[coins[0]][currencies[0]]) > 0)
        self.assertTrue(float(res[coins[0]][currencies[1]]) > 0)

    def test_get_price_multiples(self):
        res = cryptocompare.get_price(coins[0:2], currencies=currencies[0:2])
        self.assertIsNotNone(res[coins[0]])
        self.assertIsNotNone(res[coins[1]])
        self.assertIsNotNone(res[coins[0]][currencies[0]])
        self.assertIsNotNone(res[coins[0]][currencies[1]])
        self.assertIsNotNone(res[coins[1]][currencies[0]])
        self.assertIsNotNone(res[coins[1]][currencies[1]])
        self.assertTrue(float(res[coins[0]][currencies[0]]) > 0)
        self.assertTrue(float(res[coins[0]][currencies[1]]) > 0)

    def test_get_price_given_exchange(self):
        res = cryptocompare.get_price(coins[0:2], currencies=currencies[0:2], exchange='Kraken')
        # If exchange parameters fails it will return an error so next assert won't be treu
        self.assertIsNotNone(res[coins[0]])
        self.assertIsNotNone(res[coins[1]])
        self.assertIsNotNone(res[coins[0]][currencies[0]])
        self.assertIsNotNone(res[coins[0]][currencies[1]])
        self.assertIsNotNone(res[coins[1]][currencies[0]])
        self.assertIsNotNone(res[coins[1]][currencies[1]])
