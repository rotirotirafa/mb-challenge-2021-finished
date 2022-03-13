from typing import List, Dict
import requests
import pandas
import numpy

from app.settings import ALLOWED_PAIRS
from app.utils import format_timestamp_days, transform_timestamp_now
from app.utils.mongodb import mms_collection


def get_closes_from_candles(candles) -> List:
    """
    Function that extract the parameter "close" from given object
    :param candles:
    :return:
    List of Closes
    Example: ["41499.99", "414599.99", ...]
    """
    close = []
    for candle in candles.get('candles'):
        close.append(candle.get('close'))
    return close


def get_candles_from_past_year(pair: str, from_date: int, to_date: int) -> Dict:
    """
    This function is responsible to retrieve data from request given ->
    :param pair:
    :param from_date:
    :param to_date:
    :return:
    Dict with candles
    """
    mb_api = f'https://mobile.mercadobitcoin.com.br/v4/{pair}/candle?from={from_date}&to={to_date}&precision=1d'
    response = requests.get(mb_api)
    return response.json()


def seed_list(pair: str) -> List:
    """
    This function is responsible to mount the payload that will be insert in database.
    :param pair:
    :return:
    List with parameters to seed a database collection
    """
    a_year_timestamp = format_timestamp_days(365)

    candles = get_candles_from_past_year(pair, a_year_timestamp, transform_timestamp_now())

    closes = get_closes_from_candles(candles)
    numpy_array = numpy.array(closes)

    panda_series = pandas.Series(numpy_array)

    mms_20 = panda_series.rolling(20).mean()
    mms_50 = panda_series.rolling(50).mean()
    mms_200 = panda_series.rolling(200).mean()

    response = []

    for mms_pair in range(364, 0, -1):
        timestamp = candles.get('candles')[mms_pair]['timestamp']
        mms_20_key = mms_20[mms_pair]
        mms_50_key = mms_50[mms_pair]
        mms_200_key = mms_200[mms_pair]

        response.append(
            {
                'pair': pair,
                'timestamp': timestamp,
                'mms_20': mms_20_key,
                'mms_50': mms_50_key,
                'mms_200': mms_200_key
            }
        )

    return response


def seed_database():
    print('Clear old data')
    mms_collection.remove({})
    print('Old Data Cleared.')
    print('Start Seed Database')
    for pair in ALLOWED_PAIRS:
        print(f'Seeding -> {pair}')
        pair_mms_seeds = seed_list(pair)
        for pair_mms_seed in pair_mms_seeds:
            mms_collection.insert_one(pair_mms_seed)
    print('Finished Seed')


seed_database()


