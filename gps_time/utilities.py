# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/10_utilities.ipynb (unless otherwise specified).

__all__ = ['logger', 'arange_gpstime', 'validate_gps_week']

# Cell
"""Copyright 2020 The Aerospace Corporation"""

# Cell

import numpy as np

from typing import List
from logging import getLogger

from .core import GPSTime

logger = getLogger(__name__)

# Cell
def arange_gpstime(
    start_gpstime: GPSTime, duration_s: float, step_ms: float
) -> List[GPSTime]:
    """Create a list of GPSTimes in sequence.

    The purpose of this function is to create a list that represents a
    sequence of GPSTimes of the specified duration with the specified step
    size.

    This function is an analogue of the `numpy.arange()` function, but
    operates on GPSTimes.

    Parameters
    ----------
    start_gpstime : GPSTime
        The GPSTime to start the sequence
    duration_s : float
        The duration of the sequence, in seconds
    step_ms : float
        The step size, in milliseconds

    Returns
    -------
    List[GPSTime]
        The sequence of GPSTimes

    Notes
    -----
    Like `numpy.arange`, this does not include the final element. That is, if
    the start is at 0 with a duration of 5 and step of 1, the sequence would
    return [0, 1, 2, 3, 4]

    See Also
    --------
    `numpy.arange()`
    `arange_datetime()`

    Todo
    ----
    .. todo:: Determine if this still works if a np.ndarray is returned
        instead of a list

    """
    return list(start_gpstime + np.arange(0, duration_s, step_ms / 1000))

# Cell
def validate_gps_week(full_week: int, gps_week: int) -> None:
    """Validate that the week numbers are consistent.

    This function validates that the full GPS week number (i.e. the number of
    weeks since 6 Jan 1980) and the mod-1024 week numbers are consistent. If
    they are not, it raises an error.

    Parameters
    ----------
    full_week : int
        The number of weeks since 6 Jan 1980
    gps_week : int
        The mod-1024 GPS week

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the `full_week` and `gps_week` disagree

    """
    if full_week % 1024 != gps_week:
        raise ValueError(
            "".join(["Full GPS Week {} must be mod 1024 of ", "GPS Week {}"]).format(
                full_week, gps_week
            )
        )