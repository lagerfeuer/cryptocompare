#!/usr/bin/env python3
import time
import unittest
import cryptocompare
import datetime
import calendar
import os


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
        self.assertTrue("BTC" in lst.keys())
        lst = cryptocompare.get_coin_list(True)
        self.assertTrue("BTC" in lst)

    def test_get_price(self):
        coin = "BTC"
        price = cryptocompare.get_price(coin)
        self.assertCoinAndCurrInPrice(coin, "EUR", price)

        price = cryptocompare.get_price(coin, currency="USD")
        self.assertCoinAndCurrInPrice(coin, "USD", price)
        currencies = ["EUR", "USD", "GBP"]
        price = cryptocompare.get_price(coin, currency=currencies)
        self.assertCoinAndCurrInPrice(coin, currencies, price)
        coins = ["BTC", "XMR"]
        price = cryptocompare.get_price(coins, currency=currencies)
        self.assertCoinAndCurrInPrice(coins, currencies, price)

    def test_get_price_full(self):
        price = cryptocompare.get_price("ETH", full=True)
        self.assertIn("RAW", price)
        self.assertIn("ETH", price["RAW"])
        self.assertIn("EUR", price["RAW"]["ETH"])
        self.assertIn("PRICE", price["RAW"]["ETH"]["EUR"])

    def test_get_historical_price(self):
        coin = "XMR"
        curr = "EUR"
        price = cryptocompare.get_historical_price(
            "XMR", timestamp=datetime.date(2017, 6, 6)
        )
        self.assertCoinAndCurrInPrice(coin, curr, price)
        price2 = cryptocompare.get_historical_price(
            "XMR", "EUR", datetime.datetime(2017, 6, 6)
        )
        self.assertCoinAndCurrInPrice(coin, curr, price2)
        self.assertEqual(price, price2)

    def test_price_day(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_day(
            coin,
            currency=curr,
            limit=3,
            exchange="CCCAGG",
            toTs=datetime.datetime(2019, 6, 6),
        )
        for frame in price:
            self.assertIn("time", frame)

    def test_price_day_all(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_day_all(
            coin, currency=curr, exchange="CCCAGG"
        )
        self.assertTrue(len(price) > 1)
        for frame in price:
            self.assertIn("time", frame)

    def test_price_day_from(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_day_from(
            coin,
            currency=curr,
            exchange="CCCAGG",
            toTs=int(calendar.timegm(datetime.datetime(2019, 6, 6).timetuple())),
            fromTs=int(calendar.timegm(datetime.datetime(2019, 6, 4).timetuple())),
        )
        self.assertTrue(len(price) == 3)
        for frame in price:
            self.assertIn("time", frame)

    def test_price_hour(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_hour(
            coin,
            currency=curr,
            limit=3,
            exchange="CCCAGG",
            toTs=datetime.datetime(2019, 6, 6, 12),
        )
        for frame in price:
            self.assertIn("time", frame)

    def test_price_hour_from(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_hour_from(
            coin,
            currency=curr,
            exchange="CCCAGG",
            toTs=int(
                calendar.timegm(datetime.datetime(2019, 6, 6, 3, 0, 0).timetuple())
            ),
            fromTs=int(
                calendar.timegm(datetime.datetime(2019, 6, 6, 1, 0, 0).timetuple())
            ),
        )
        self.assertTrue(len(price) == 3)
        for frame in price:
            self.assertIn("time", frame)

    def test_price_minute(self):
        coin = "BTC"
        curr = "USD"
        price = cryptocompare.get_historical_price_minute(
            coin,
            currency=curr,
            limit=3,
            exchange="CCCAGG",
            toTs=datetime.datetime.now(),
        )
        for frame in price:
            self.assertIn("time", frame)

    def test_get_avg(self):
        coin = "BTC"
        curr = "USD"
        avg = cryptocompare.get_avg(coin, curr, exchange="Kraken")
        self.assertEqual(avg["LASTMARKET"], "Kraken")
        self.assertEqual(avg["FROMSYMBOL"], coin)
        self.assertEqual(avg["TOSYMBOL"], curr)

    def test_get_exchanges(self):
        exchanges = cryptocompare.get_exchanges()
        self.assertIn("Kraken", exchanges)

    def test_get_pairs(self):
        pairs = cryptocompare.get_pairs(exchange="Kraken")
        self.assertEqual("Kraken", pairs[0]["exchange"])

    def test_sets_api_key_using_environment_variable(self):
        os.environ["CRYPTOCOMPARE_API_KEY"] = "Key"
        api_key_parameter = cryptocompare.cryptocompare._set_api_key_parameter(None)
        assert api_key_parameter == "&api_key=Key"

    def test_sets_api_key_with_no_env_var_and_none_passed(self):
        if os.getenv("CRYPTOCOMPARE_API_KEY"):
            del os.environ["CRYPTOCOMPARE_API_KEY"]
        api_key_parameter = cryptocompare.cryptocompare._set_api_key_parameter(None)
        assert api_key_parameter == ""

    def test_sets_api_key_passed_in_works(self):
        api_key_parameter = cryptocompare.cryptocompare._set_api_key_parameter(
            "keytest"
        )
        assert api_key_parameter == "&api_key=keytest"


if __name__ == "__main__":
    unittest.main()
