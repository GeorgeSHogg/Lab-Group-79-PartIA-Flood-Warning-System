from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()
    N = 9
    rivers_by_station_number(stations, N)

run()

