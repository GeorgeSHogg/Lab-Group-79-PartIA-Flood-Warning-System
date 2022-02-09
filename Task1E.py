from tkinter import N
from floodsystem.geo import rivers_by_station_number_dict
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""
    stations = build_station_list()

    print(rivers_by_stations_number_dict(stations, N))

run()
