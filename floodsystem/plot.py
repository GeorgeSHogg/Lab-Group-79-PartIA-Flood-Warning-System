import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import numpy as np

def plot_water_levels(station, dates, levels):

    low, high = station.typical_range

#Plot with axes
    plt.plot(dates, levels)
    plt.axhline(y = low, color = "g")
    plt.axhline(y = high, color = "r")

#Added titles and labelled axes onto plots
    plt.xlabel("Time for a station (days)")
    plt.ylabel("Water Level (m)")
    plt.title(station)
    plt.xticks(rotation = 90)
    plt.title("Station: " + station.name)
#Display plot
    plt.tight_layout()
    plt.show()