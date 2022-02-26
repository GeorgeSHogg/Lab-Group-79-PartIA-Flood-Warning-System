import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import numpy as np

def plot_water_levels(station, dates, levels):

    station = build_station_list()
    dates = []
    levels = []
    low = station.get_typical_range()[0]
    high = station.get_typical_range()[1]

#Plot with axes
    plt.plot(dates, levels)
    plt.plot(dates, low)
    plt.plot(dates, high)

#Added titles and labelled axes onto plots
    plt.xlabel("Time for a station (days)")
    plt.ylabel("Water Level (m)")
    plt.title(station)
    plt.xticks(rotation = 90)
    plt.title("Station: " + station.get_stationName())

#Display plot
    plt.tight_layout()
    plt.show()