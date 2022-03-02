"""Unit test for the plot module"""

from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels

test_station = MonitoringStation()
station_id = 3
measure_id = 10
coord = (float(0.4), float(2.6))
typical_range = (0.3, 1.3)
river = "Nile"
town = "London"


def test_plot_water_levels():
    dates, levels = [], []
    # testing that when an empty dates or levels list is inputted then no graph is plotted
    assert plot_water_levels(test_station, dates, levels) == 'The test_station has empty levels or dates list'

def test_plot_water_level_with_fit():
    dates, levels = [], []
    # testing that when an empty dates or levels list is inputted then no graph is plotted
    assert plot_water_levels(test_station, dates, levels) == 'The test_station has empty levels or dates list'