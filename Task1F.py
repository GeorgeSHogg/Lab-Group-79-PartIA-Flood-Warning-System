from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations)
    print(sorted([station.name for station in stations]))


if __name__ == "__main__":
    print("Task 1F")
    run()