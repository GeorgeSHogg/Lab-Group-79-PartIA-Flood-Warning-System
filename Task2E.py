from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import most_at_risk_stations
import matplotlib.pyplot as plt
import datetime
import numpy as np

def run():
    """Requirements for Task 2E"""

    stations = build_station_list()
    update_water_levels(stations)
    stations_used = []
    highest_level_stations = most_at_risk_stations(stations, 10)

    station_list = []
    dates_list = []
    levels_list = []

    for station in highest_level_stations:
        stations_used.append(station[0])

    for station in stations_used:
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=10))
        if len(dates) > 3:
            dates = np.array(dates)
            levels = np.array(levels)
            plot_water_levels([station], [dates] , [levels])

            station_list.append(station)
            dates_list.append(dates)
            levels_list.append(levels)

    plot_water_levels(station_list[:5], dates_list[:5], levels_list[:5], False)

if __name__ == "__main__":
    print("***Task 2E: CUED Part 1A Flood Warning System")
    run()