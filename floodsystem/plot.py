import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit
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

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates,levels,p)
    
    #Plot with axes
    low, high = station.typical_range
    plt.axhline(y = low, color = "g", label = station.name + " low")
    plt.axhline(y = high, color = "r", label = station.name + " high")
    plt.plot(matplotlib.dates.date2num(dates),levels)
    plt.plot (dates, poly(matplotlib.dates.date2num(dates)-d0))

    #Added titles and labelled axes onto plots
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 90)
    plt.title(station.name)
    plt.show()