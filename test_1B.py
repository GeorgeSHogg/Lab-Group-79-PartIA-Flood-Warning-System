from floodsystem.geo import stations_by_distance
from floodsystem.geo import distance
from floodsystem.stationdata import build_station_list
import numpy as np

def test_distance():
    d1 = distance((0, 180), (0, 0))
    d2 = np.pi * 6371
    print(d1)
    print(d2)
    assert np.isclose(d1, d2)

def test_distance_sorter():
    p = (52.2053, 0.1218)
    stations = build_station_list()
    sorted_stations = stations_by_distance(stations, p)
    prev_distance = 0
    for station in sorted_stations:
        assert station[1] >= prev_distance
        prev_distance = station[1]

test_distance()
test_distance_sorter()