cryptocompare
#############

Python3 Wrapper to query cryptocurrency prices (and more) using the CryptoCompare_ API.

Installation
************

.. code:: bash
   
   sudo pip install cryptocompare

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
   cryptocompare.get_historical_price('XMR', timestamp=datetime.datetime(2017,6,6))
   # or
   cryptocompare.get_historical_price('XMR', curr='EUR', datetime.datetime(2017,6,6))

   # {'XMR': {'EUR': 43.05}}



.. _Cryptocompare: https://www.cryptocompare.com/

