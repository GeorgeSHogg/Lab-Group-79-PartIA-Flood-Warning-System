from floodsystem.flood import most_at_risk_stations, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def breakdown(station):
    station, level = station
    return(str(station.name) + " " + str(level))

def run():
    "Requirements for Task 2B"
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    at_risk = most_at_risk_stations(stations, N)
    sorted_at_risk = [breakdown(station) for station in at_risk]
    print(*sorted_at_risk, sep = "\n")

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
