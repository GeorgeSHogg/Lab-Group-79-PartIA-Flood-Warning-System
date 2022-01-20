from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    r = 10
    p = (52.2053, 0.1218)
    stations = build_station_list()

    stations = stations_within_radius(stations, p, r)
    print(sorted([station.name for station in stations]))

if __name__ == "__main__":
    print("Task 1C")
    run()