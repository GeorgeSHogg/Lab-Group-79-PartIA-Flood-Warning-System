from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np

def test_tol_and_order():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    at_risk = stations_level_over_threshold(stations, tol)
    prev_value = np.inf
    for station in at_risk:
        _, cur_value = station 
        assert prev_value > cur_value
        assert cur_value > tol