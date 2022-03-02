"""Unit test for the analysis module"""

from floodsystem.analysis import polyfit

test_dates = [5, 4, 3, 2, 1, 0]
test_levels = [0, 1, 4, 9, 16, 25]


def test_polyfit():
    poly, d0 = polyfit(test_dates, test_levels, 2)
    assert round(poly(2)) == 9