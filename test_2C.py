from floodsystem.flood import most_at_risk_stations, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np

def test_tol_and_order():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    at_risk = most_at_risk_stations(stations, N)
    prev_value = np.inf
    assert len(at_risk) == N
    for station in at_risk:
        _, cur_value = station 
        assert prev_value >= cur_value
