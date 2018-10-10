import requests
import time
import datetime

# API
URL_COIN_LIST = 'https://www.cryptocompare.com/api/data/coinlist/'
URL_PRICE = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
URL_PRICE_MULTI = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
URL_PRICE_MULTI_FULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'
URL_HIST_PRICE = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}&e={}'
URL_HIST_PRICE_DAY = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}'
URL_HIST_PRICE_HOUR = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}'
URL_HIST_PRICE_MINUTE = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}'
URL_AVG = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym={}&e={}'
URL_EXCHANGES = 'https://www.cryptocompare.com/api/data/exchanges'

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
LIMIT = 1440
###############################################################################

def query_cryptocompare(url,errorCheck=True, *args, **kwargs):
    try:
        response = requests.get(url, *args, **kwargs).json()
    except Exception as e:
        print('Error getting coin information. %s' % str(e))
        return None
    if errorCheck and (response.get('Response') == 'Error'):
        print('[ERROR] %s' % response.get('Message'))
        return None
    return response

def format_parameter(parameter):
    if isinstance(parameter, list):
        return ','.join(parameter)
    else:
        return parameter

###############################################################################

def get_coin_list(format=False, *args, **kwargs):
    response = query_cryptocompare(URL_COIN_LIST, False, *args, **kwargs)['Data']
    if format:
        return list(response.keys())
    else:
        return response

# TODO: add option to filter json response according to a list of fields
def get_price(coin, curr=CURR, full=False, *args, **kwargs):
    if full:
        return query_cryptocompare(URL_PRICE_MULTI_FULL.format(format_parameter(coin),
            format_parameter(curr)), *args, **kwargs)
    if isinstance(coin, list):
        return query_cryptocompare(URL_PRICE_MULTI.format(format_parameter(coin),
            format_parameter(curr)), *args, **kwargs)
    else:
        return query_cryptocompare(URL_PRICE.format(coin, format_parameter(curr)), *args, **kwargs)

def get_historical_price(coin, curr=CURR, timestamp=time.time(), exchange='CCCAGG', *args, **kwargs):
    if isinstance(timestamp, datetime.datetime):
        timestamp = time.mktime(timestamp.timetuple())
    return query_cryptocompare(URL_HIST_PRICE.format(coin, format_parameter(curr),
        int(timestamp), format_parameter(exchange)), *args, **kwargs)

def get_historical_price_day(coin, curr=CURR, *args, **kwargs):
    return query_cryptocompare(URL_HIST_PRICE_DAY.format(coin, format_parameter(curr)), *args, **kwargs)

def get_historical_price_hour(coin, curr=CURR, *args, **kwargs):
    return query_cryptocompare(URL_HIST_PRICE_HOUR.format(coin, format_parameter(curr)), *args, **kwargs)

def get_historical_price_minute(coin, curr=CURR, limit=LIMIT, *args, **kwargs):
    return query_cryptocompare(URL_HIST_PRICE_MINUTE.format(coin, format_parameter(curr), limit), *args, **kwargs)

def get_avg(coin, curr=CURR, exchange='CCCAGG', *args, **kwargs):
    response = query_cryptocompare(URL_AVG.format(coin, curr, format_parameter(exchange)), *args, **kwargs)
    if response:
        return response['RAW']

def get_exchanges(*args, **kwargs):
    response = query_cryptocompare(URL_EXCHANGES, *args, **kwargs)
    if response:
        return response['Data']
