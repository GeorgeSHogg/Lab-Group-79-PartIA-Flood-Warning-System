from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import distance

def test_radius():
    r = 10
    p = (52.2053, 0.1218)
    stations = build_station_list()
    stations = stations_within_radius(stations, p, r)
    for station in stations:
        assert distance(station.coord, p) <= r