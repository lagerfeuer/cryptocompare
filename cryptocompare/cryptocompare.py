import sys
import requests
import time
import datetime

# API
URL_COIN_LIST = 'https://www.cryptocompare.com/api/data/coinlist/'
URL_PRICE = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
URL_PRICE_MULTI = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
URL_PRICE_MULTI_FULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'
URL_HIST_PRICE = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}'

# FIELDS
PRICE = 'PRICE'
HIGH = 'HIGH24HOUR'
LOW = 'LOW24HOUR'
VOLUME = 'VOLUME24HOUR'
CHANGE = 'CHANGE24HOUR'
CHANGE_PERCENT = 'CHANGEPCT24HOUR'
MARKETCAP = 'MKTCAP'

# DEFAULTS
CURR = 'EUR'

###############################################################################

def query_cryptocompare(url):
    try:
        return requests.get(url).json()
    except Exception as e:
        sys.exit('Error getting coin information. %s' % str(e))

def format_parameter(parameter):
    if isinstance(parameter, list):
        return ','.join(parameter)
    else:
        return parameter

###############################################################################

# TODO: add formatting option, if true, it only returns a list of coin names
def get_coin_list(format=False):
    return query_cryptocompare(URL_COIN_LIST)['Data']

# TODO: add option to filter json response according to a list of fields
def get_price(coin, curr=CURR, full=False):
    if full:
        return query_cryptocompare(URL_PRICE_MULTI_FULL.format(format_parameter(coin), format_parameter(curr)))
    if isinstance(coin, list):
        return query_cryptocompare(URL_PRICE_MULTI.format(format_parameter(coin), format_parameter(curr)))
    else:
        return query_cryptocompare(URL_PRICE.format(coin, format_parameter(curr)))

def get_historical_price(coin, curr=CURR, timestamp=time.time()):
    if isinstance(timestamp, datetime.datetime):
        timestamp = time.mktime(timestamp.timetuple())
    return query_cryptocompare(URL_HIST_PRICE.format(coin, format_parameter(curr), int(timestamp)))

def get_avg(coins, curr=CURR):
    pass

def histo_day(coin):
    pass
def hist_hour(coin):
    pass
def hist_minute(coin):
    pass

