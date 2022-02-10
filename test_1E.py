from distutils.command.build import build
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def test_rivers_by_station_number():

    stations = build_station_list()
    N = 9
    river_dict = rivers_by_station_number(stations, N)
    prev_value = 999999999999999999999999999999
    for river in river_dict:
        river_name, river_value = river
        assert river_value <= prev_value
        prev_value = river_value
