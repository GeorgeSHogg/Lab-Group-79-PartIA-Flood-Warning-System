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

    for station in highest_level_stations:
        stations_used.append(station[0])

    for station in stations_used:
        print(station.measure_id)
        print(station)
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=10))
        print(dates)
        dates = np.array(dates)
        levels = np.array(levels)
        print(dates.shape)
        print(levels.shape)
        plot_water_levels(station,dates,levels)
        plt.show()

if __name__ == "__main__":
    print("***Task 2E: CUED Part 1A Flood Warning System")
    run()