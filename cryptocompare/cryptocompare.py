import requests
import time
import datetime

# API - https://min-api.cryptocompare.com/
__URL_COIN_LIST = 'https://min-api.cryptocompare.com/data/all/coinlist'
__URL_RATE_LIMITS = 'https://min-api.cryptocompare.com/stats/rate/limit'
__URL_EXCHANGES = 'https://min-api.cryptocompare.com/data/all/exchanges'
__URL_HIST_PRICE = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}&e={}'
__URL_HIST_PRICE_DAY = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&e={}&aggregate={}'
__URL_HIST_PRICE_HOUR = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&e={}&aggregate={}'
__URL_HIST_PRICE_MINUTE = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&e={}&aggregate={}'
__URL_DAY_AVG = 'https://min-api.cryptocompare.com/data/dayAvg?fsym={}&tsym={}&e={}'
__URL_AVG = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym={}&e={}'
__URL_PRICE = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}&e={}'
__URL_PRICE_MULTI_FULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}&e={}'

# DEFAULTS
DEFAULT_CURRENCY = 'USD'
DEFAULT_LIMIT_DAY = '30'
DEFAULT_LIMIT_HOUR = '24'
DEFAULT_LIMIT_MINUTE = '30'
DEFAULT_AGGREGATE = '1' # 1 means not aggregate prices
DEFAULT_EXCHANGE = 'CCCAGG'     # Match average in CryptoCompare


def __query_cryptocompare(url, errorCheck=True):
    try:
        response = requests.get(url).json()
    except Exception as e:
        print('Error getting coin information. %s' % str(e))
        return None
    if errorCheck and (response.get('Response') == 'Error'):
        print('[ERROR] %s' % response.get('Message'))
        return None
    return response


def __format_parameter(parameter):
    if isinstance(parameter, list):
        return ','.join(parameter)
    else:
        return parameter


def get_coin_list():
    return __query_cryptocompare(__URL_COIN_LIST, False)['Data']


def get_rate_limit_all():
    return __query_cryptocompare(__URL_RATE_LIMITS, False)


def get_rate_limit_hour():
    return __query_cryptocompare(__URL_RATE_LIMITS, False)['Hour']


def get_rate_limit_minute():
    return __query_cryptocompare(__URL_RATE_LIMITS, False)['Minute']


def get_rate_limit_second():
    return __query_cryptocompare(__URL_RATE_LIMITS, False)['Second']


def get_exchanges():
    return __query_cryptocompare(__URL_EXCHANGES)


def get_historical_price(coin, currency=DEFAULT_CURRENCY, timestamp=time.time(), exchange=DEFAULT_EXCHANGE):
    if isinstance(timestamp, datetime.datetime):
        timestamp = time.mktime(timestamp.timetuple())
    return __query_cryptocompare(__URL_HIST_PRICE.format(coin, currency, int(timestamp), exchange))


def get_historical_price_day(coin, currency=DEFAULT_CURRENCY, limit=DEFAULT_LIMIT_DAY, aggregate=DEFAULT_AGGREGATE,
                             exchange=DEFAULT_EXCHANGE):
    return __query_cryptocompare(__URL_HIST_PRICE_DAY.format(coin, currency, str(limit), exchange, aggregate))


def get_historical_price_hour(coin, currency=DEFAULT_CURRENCY, limit=DEFAULT_LIMIT_HOUR, exchange=DEFAULT_EXCHANGE,
                              aggregate=DEFAULT_AGGREGATE):
    return __query_cryptocompare(__URL_HIST_PRICE_HOUR.format(coin, currency, str(limit), exchange, aggregate))


def get_historical_price_minute(coin, currency=DEFAULT_CURRENCY, limit=DEFAULT_LIMIT_MINUTE, exchange=DEFAULT_EXCHANGE,
                                aggregate=DEFAULT_AGGREGATE):
    return __query_cryptocompare(__URL_HIST_PRICE_MINUTE.format(coin, currency, str(limit), exchange, aggregate))


def get_daily_avg(coin, currency=DEFAULT_CURRENCY, exchange=DEFAULT_EXCHANGE):
    return __query_cryptocompare(__URL_DAY_AVG.format(coin, currency, exchange))


def get_avg(coin, currency=DEFAULT_CURRENCY, exchange=DEFAULT_EXCHANGE):
    return __query_cryptocompare(__URL_AVG.format(coin, curr, exchange))['RAW']


def get_price(coins, currencies=DEFAULT_CURRENCY, exchange=DEFAULT_EXCHANGE, full=False):
    if full:
        return __query_cryptocompare(__URL_PRICE_MULTI_FULL.format(__format_parameter(coins),
                                                                   __format_parameter(currencies), exchange))
    else:
        return __query_cryptocompare(__URL_PRICE.format(__format_parameter(coins),
                                                        __format_parameter(currencies), exchange))
