"""Unit test for the analysis module"""

from floodsystem.analysis import polyfit
import numpy as np

a, b, c = 3, 5, 9

train_dates = np.arange(0, 12)
train_levels = a * np.square(train_dates) + b * train_dates + c

def test_polyfit():
    poly, d0 = polyfit(train_dates, train_levels, 3, False)

    test_dates = np.arange(19, 43)
    test_levels = a * np.square(test_dates) + b * test_dates + c
    assert all(np.isclose(test_levels, poly(test_dates)))
