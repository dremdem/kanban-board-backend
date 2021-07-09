"""
Helpers for do some calculations.

Import as:

import task.utils as utils
"""

import datetime as dt
import decimal

import task.constants as const


def get_time_by_delta(delta: dt.timedelta) -> str:
    """
    Calculate the time representation by then given delta.

    :param delta: Datetime delta.
    :return: Datetime with the mask: <HH:MM:SS>
    """
    days, seconds = delta.days, delta.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "%02d:%02d:%02d" % (hours, minutes, seconds)


def get_cost_by_delta(delta: dt.timedelta) -> decimal.Decimal:
    """
    Calculate the cost by the given delta.

    :param delta: Datetime delta.
    :return: Cost as Decimal.
    """
    hours = delta.seconds / 60 / 60
    decimal.getcontext().prec = 3
    return decimal.Decimal(hours) * decimal.Decimal(const.HOURLY_RATE)
