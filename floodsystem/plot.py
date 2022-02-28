import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import numpy as np

def plot_water_levels(station_list, dates_list, levels_list, plot_typical = True):

    title = ""

    for station, dates, levels in zip(station_list, dates_list, levels_list):
        
        title = title + station.name + " "
        #Plot with axes
        plt.plot(dates, levels, label = station.name)
        
        if plot_typical:
            low, high = station.typical_range
            plt.axhline(y = low, color = "g", label = station.name + " low")
            plt.axhline(y = high, color = "r", label = station.name + " high")

    #Added titles and labelled axes onto plots
    plt.title(title)
    plt.xlabel("Time for a station (days)")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation = 90)

    plt.title("Station(s): " + title)
    #Display plot
    plt.tight_layout()
    plt.show()