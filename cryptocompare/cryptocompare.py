"""
CryptoCompare API wrapper
"""
import requests
import time
import datetime
import typing
import os
from typing import Union, Optional, List, Dict
Timestamp = Union[datetime.datetime, datetime.date, int, float]

# API
_API_KEY_PARAMETER = ""
_URL_COIN_LIST = 'https://www.cryptocompare.com/api/data/coinlist?'
_URL_PRICE = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
_URL_PRICE_MULTI = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms={}'
_URL_PRICE_MULTI_FULL = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms={}'
_URL_HIST_PRICE = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}&e={}'
_URL_HIST_PRICE_DAY = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_HIST_PRICE_HOUR = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_HIST_PRICE_MINUTE = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&e={}&toTs={}'
_URL_AVG = 'https://min-api.cryptocompare.com/data/generateAvg?fsym={}&tsym={}&e={}'
_URL_EXCHANGES = 'https://www.cryptocompare.com/api/data/exchanges?'
_URL_PAIRS = 'https://min-api.cryptocompare.com/data/pair/mapping/exchange?e={}'

# DEFAULTS
CURRENCY = 'EUR'
LIMIT = 1440
###############################################################################


def _query_cryptocompare(url: str, errorCheck: bool = True, api_key: str = None) -> Optional[Dict]:
    """
    Query the url and return the result or None on failure.

    :param url: the url
    :param errorCheck: run extra error checks (default: True)
    :returns: respones, or nothing if errorCheck=True
    :api_key: optional, if you want to add an API Key
    """
    api_key_parameter = _set_api_key_parameter(api_key)
    try:
        response = requests.get(url + api_key_parameter).json()
    except Exception as e:
        print('Error getting coin information. %s' % str(e))
        return None
    if errorCheck and (response.get('Response') == 'Error'):
        print('[ERROR] %s' % response.get('Message'))
        return None
    return response


def _format_parameter(parameter: object) -> str:
    """
    Format the parameter depending on its type and return
    the string representation accepted by the API.

    :param parameter: parameter to format
    """
    if isinstance(parameter, list):
        return ','.join(parameter)

    else:
        return str(parameter)


def _format_timestamp(timestamp: Timestamp) -> int:
    """
    Format the timestamp depending on its type and return
    the integer representation accepted by the API.

    :param timestamp: timestamp to format
    """
    if isinstance(timestamp, datetime.datetime) or isinstance(timestamp, datetime.date):
        return int(time.mktime(timestamp.timetuple()))
    return int(timestamp)


def _set_api_key_parameter(api_key: str = None) -> str:
    if api_key is None:
        api_key = os.getenv('CRYPTOCOMPARE_API_KEY')
    if api_key is not None:
        _API_KEY = "&api_key={}".format(api_key)
        return _API_KEY
    return ""

###############################################################################


def get_coin_list(format: bool = False) -> Union[Dict, List, None]:
    """
    Get the coin list (all available coins).

    :param format: format as python list (default: False)
    :returns: dict or list of available coins
    """
    response = _query_cryptocompare(_URL_COIN_LIST, False)
    if response:
        response = typing.cast(Dict, response['Data'])
        return list(response.keys()) if format else response
    return None

# TODO: add option to filter json response according to a list of fields


def get_price(coin: str, currency: str = CURRENCY, full: bool = False) -> Optional[Dict]:
    """
    Get the currencyent price of a coin in a given currency.

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param full: full response or just the price (default: False)
    :returns: dict of coin and currency price pairs
    """
    if full:
        return _query_cryptocompare(
            _URL_PRICE_MULTI_FULL.format(
                _format_parameter(coin), _format_parameter(currency))
        )
    if isinstance(coin, list):
        return _query_cryptocompare(
            _URL_PRICE_MULTI.format(_format_parameter(coin),
                                    _format_parameter(currency))
        )
    return _query_cryptocompare(
        _URL_PRICE.format(coin, _format_parameter(currency))
    )


def get_historical_price(coin: str, currency: str = CURRENCY, timestamp: Timestamp = time.time(),
                         exchange: str = 'CCCAGG') -> Optional[Dict]:
    """
    Get the price of a coin in a given currency during a specific time.

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param timestamp: point in time
    :param exchange: the exchange to use
    :returns: dict of coin and currency price pairs
    """
    return _query_cryptocompare(
        _URL_HIST_PRICE.format(coin,
                               _format_parameter(currency),
                               _format_timestamp(timestamp),
                               _format_parameter(exchange))
    )


def get_historical_price_day(coin: str, currency: str = CURRENCY, limit: int = LIMIT,
                             exchange: str = 'CCCAGG', toTs: Timestamp = time.time()) -> Optional[Dict]:
    """
    Get historical price (day).

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param limit: number of data points (max. 2000)
    :param exchange: exchange to use (default: 'CCCAGG')
    :param toTs: return data before this timestamp. (Unix epoch time or datetime object)
    :returns: dict of coin and currency price pairs
    """
    response = _query_cryptocompare(
        _URL_HIST_PRICE_DAY.format(coin, _format_parameter(currency), limit, exchange, _format_timestamp(toTs)))
    if response:
        return response['Data']
    return None


def get_historical_price_hour(coin: str, currency: str = CURRENCY, limit: int = LIMIT,
                              exchange: str = 'CCCAGG', toTs: Timestamp = time.time()) -> Optional[Dict]:
    """
    Get historical price (hourly).


    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param limit: number of data points (max. 2000)
    :param exchange: exchange to use (default: 'CCCAGG')
    :param toTs: return data before this timestamp. (Unix epoch time or datetime object)
    :returns: dict of coin and currency price pairs
    """
    response = _query_cryptocompare(
        _URL_HIST_PRICE_HOUR.format(coin, _format_parameter(currency), limit, exchange, _format_timestamp(toTs)))
    if response:
        return response['Data']
    return None


def get_historical_price_minute(coin: str, currency: str = CURRENCY, limit: int = LIMIT,
                                exchange: str = 'CCCAGG', toTs: Timestamp = time.time()) -> Optional[Dict]:
    """
    Get historical price (minute).

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param limit: number of data points (max. 2000)
    :param exchange: exchange to use (default: 'CCCAGG')
    :param toTs: return data before this timestamp. (Unix epoch time or datetime object)
    :returns: dict of coin and currency price pairs
    """
    response = _query_cryptocompare(
        _URL_HIST_PRICE_MINUTE.format(coin, _format_parameter(currency), limit, exchange, _format_timestamp(toTs)))
    if response:
        return response['Data']
    return None


def get_avg(coin: str, currency: str = CURRENCY, exchange: str = 'CCCAGG') -> Optional[Dict]:
    """
    Get the average price

    :param coin: symbolic name of the coin (e.g. BTC)
    :param currency: short hand description of the currency (e.g. EUR)
    :param exchange: exchange to use (default: 'CCCAGG')
    :returns: dict of coin and currency price pairs
    """
    response = _query_cryptocompare(_URL_AVG.format(
        coin, currency, _format_parameter(exchange)))
    if response:
        return response['RAW']
    return None


def get_exchanges() -> Optional[Dict]:
    """
    Get the list of available exchanges.

    :returns: list of available exchanges
    """
    response = _query_cryptocompare(_URL_EXCHANGES)
    if response:
        return response['Data']
    return None


def get_pairs(exchange: str = None) -> Optional[Dict]:
    """
    Get the list of available pairs for a particular exchange or for 
    all exchanges (if exchange is None)

    :param exchange: exchange to use (default: None)
    :returns: list of available exchanges
    """
    if exchange is None:
        response = _query_cryptocompare(_URL_PAIRS.split('?')[0])

    else:
        response = _query_cryptocompare(_URL_PAIRS.format(exchange))
    if response:
        return response['Data']
    return None
