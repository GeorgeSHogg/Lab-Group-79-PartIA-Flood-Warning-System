from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def breakdown(station):
    station, level = station
    return(str(station.name) + " " + str(level))

def run():
    "Requirements for Task 2B"
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    at_risk = stations_level_over_threshold(stations, tol)
    at_risk = [breakdown(station) for station in at_risk]
    print(*at_risk, sep = "\n")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
