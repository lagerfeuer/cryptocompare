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

Coin List
---------

.. code:: python

   cryptocompare.get_coin_list(format=False)

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

If ``format`` is ``True``, the coin list is returned as Python list.

Price
-----
.. code:: python

   cryptocompare.get_price('BTC')
   # or
   cryptocompare.get_price('BTC',curr='USD',full=True)
   # or
   cryptocompare.get_price(['BTC','ETH'],['EUR','GBP'])

   # {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
   #  'ETH': {'EUR': 258.1, 'GBP': 241.25}}

Historical Price
----------------
.. code:: python

   # pass either datetime or time instance
   cryptocompare.get_historical_price('XMR', timestamp=datetime.datetime(2017,6,6), exchange='CCCAGG')
   # or
   cryptocompare.get_historical_price('XMR', 'EUR', datetime.datetime(2017,6,6))

   # {'XMR': {'EUR': 43.05}}

Day
---
.. code:: python

   cryptocompare.get_historical_price_day('BTC', curr='EUR')

Hour
----
.. code:: python

   cryptocompare.get_historical_price_hour('BTC', curr='EUR')

   
Minute
------
.. code:: python

   cryptocompare.get_historical_price_minute('BTC', curr='EUR')
   cryptocompare.get_historical_price_minute('BTC', curr='EUR', limit=1440)

Average
-------

.. code:: python

   cryptocompare.get_avg('BTC', curr='EUR', exchange='Kraken')

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


Exchanges
---------

.. code:: python

   cryptocompare.get_exchanges()


Credit
******

Thanks to CryptoCompare_ for providing this service.

.. _Cryptocompare: https://min-api.cryptocompare.com/

Disclaimer
**********

This is a hobby project, no guarantees. If you find bugs, open an issue. If you want additional features, open an issue or create a pull request.
