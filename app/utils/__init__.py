import time
import pandas
from datetime import datetime, timedelta

from app.exceptions import TimeRangeIsNotValid


def transform_timestamp_now() -> int:
	"""
	Get timestamp from now
	:return:
	"""
	timestamp_now = time.time()
	return int(timestamp_now)


def format_timestamp_days(days: int) -> int:
	"""
	given a days transform in timestamp the result
	:param days:
	:return:
	"""
	now = datetime.now()
	delta_time = timedelta(days=days)
	delta_wanted = now - delta_time
	timestamp_result = datetime.timestamp(delta_wanted)
	return int(timestamp_result)


def verify_if_timestamp_is_more_than_year(timestamp: int):
	"""
	Check if the timestamp is allowed to proceed with query.
	:param timestamp:
	:return: if timestamp is more than 365 days this function will raise an error: TimeRangeIsNotValid()
	"""
	date_time = datetime.fromtimestamp(timestamp)

	delta_time = datetime.now() - timedelta(days=365)

	date_list = pandas.date_range(delta_time, periods=365, normalize=True).to_list()

	formatted_date_time = date_time.strftime('%Y-%m-%d')
	formatted_date_list = [d.strftime('%Y-%m-%d') for d in date_list]

	if formatted_date_time not in formatted_date_list:
		raise TimeRangeIsNotValid(message='Não é permitido consultas anterior à 365 dias.', errors='Not Allowed')

	return
