from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    "Requirements for Task 1E"
    """Build a list of stations"""
    stations = build_station_list()
    N = 9
    most_stations = rivers_by_station_number(stations, N)
    print(len(most_stations), " Stations found")
    print(most_stations)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()

