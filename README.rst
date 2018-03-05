cryptocompare
#############

Python3 Wrapper to query cryptocurrency prices (and more) using the CryptoCompare_ API.

Installation
************

.. code:: bash

   sudo pip3 install cryptocompare

Usage
*****

Import
======

.. code:: python

   import cryptocompare

Methods
=======

Price
-----
.. code:: python

   cryptocompare.get_price('BTC')
   # or
   cryptocompare.get_price('BTC',curr='USD',full=True)
   # or
   cryptocompare.get_price('BTC',curr='USD', full=True, exchange='Kraken')
   # or
   cryptocompare.get_price(['BTC','ETH'], ['EUR','GBP'])

   # {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
   #  'ETH': {'EUR': 258.1, 'GBP': 241.25}}

Coin List
---------

.. code:: python

   cryptocompare.get_coin_list()

   # ...
   # },
   # 'BTC': {
   #  'Id': '1182'
   #  'Url': '/coins/btc/overview'
   #  'ImageUrl': '/media/19633/btc.png'
   #  'Name': 'BTC'
   #  'CoinName': 'Bitcoin'
   #  'FullName': 'Bitcoin (BTC)'
   #  'Algorithm': 'SHA256'
   #  'ProofType': 'PoW'
   #  'FullyPremined': '0'
   #  'TotalCoinSupply': '21000000'
   #  'PreMinedValue': 'N/A'
   #  'TotalCoinsFreeFloat': 'N/A'
   #  'SortOrder': '1'
   # },
   # ...


Average
-------

.. code:: python

   cryptocompare.get_avg('BTC', currency='EUR', exchange='Kraken')

   # {
   # 'MARKET': 'CUSTOMAGG',
   # 'FROMSYMBOL': 'BTC',
   # 'TOSYMBOL': 'EUR',
   # 'FLAGS': 0,
   # 'PRICE': 3610,
   # 'LASTUPDATE': 1503066719,
   # 'LASTVOLUME': 0.5,
   # 'LASTVOLUMETO': 1805,
   # 'LASTTRADEID': 1503066719.7584,
   # 'VOLUME24HOUR': 12614.509997469995,
   # 'VOLUME24HOURTO': 46397723.00499387,
   # 'OPEN24HOUR': 3847.9,
   # 'HIGH24HOUR': 3848.96,
   # 'LOW24HOUR': 3555,
   # 'LASTMARKET': 'Kraken',
   # 'CHANGE24HOUR': -237.9000000000001,
   # 'CHANGEPCT24HOUR': -6.182593102731363
   # }

Historical Price
----------------
.. code:: python

   # pass either datetime or time instance
   cryptocompare.get_historical_price('XMR', timestamp=datetime.datetime(2017,6,6))
   # or
   cryptocompare.get_historical_price('XMR', 'EUR', datetime.datetime(2017,6,6))

   # {'XMR': {'EUR': 43.05}}

Day
---
.. code:: python

   cryptocompare.get_historical_price_day('BTC', currency='EUR')
   # or
   cryptocompare.get_historical_price_day('BTC', currency='EUR', exchange='Kraken')
   # or
   cryptocompare.get_historical_price_day('BTC', currency='EUR', limit=30)
   # or
   cryptocompare.get_historical_price_day('BTC', currency='EUR', exchange='Kraken', aggregate=5)

Hour
----
.. code:: python

   cryptocompare.get_historical_price_hour('BTC', currency='EUR')

Minute
----
.. code:: python

cryptocompare.get_historical_price_hour('BTC', currency='EUR')

Exchanges
---------

.. code:: python

   cryptocompare.get_exchanges()

API Rate Limits
---------------
.. code:: python
   cryptocompare.get_rate_limit_all()
   # or
   cryptoCompare.get_rate_limit_hour()
   # or
   cryptoCompare.get_rate_limit_minute()
   # or
   cryptoCompare.get_rate_limit_second()


For more examples check Unittests

Credit
******

Thanks to CryptoCompare_ for providing this service and building a community around everything crypto related.

Tipjar
******

If you like this and/or use it in a project, show some love:

BTC: ``1JJMk3QmcyTjPsvFpKUhgvPNd3KcWCKc86``

ETH: ``0xe3c951a953f56d0ec88800386281e88ea9bef630``

...or head over to https://www.cryptocompare.com and tip CryptoCompare_.

.. _Cryptocompare: https://www.cryptocompare.com/

Disclaimer
**********

This is a hobby project, no guarantees. If you find bugs, open an issue. If you want additional features, open an issue or create a pull request.
