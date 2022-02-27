import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):


    low, high = station.typical_range

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

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates,levels,p)
    typical_high = station.typical_range[1]
    typical_low = station.typical_range[0]
    high=[]
    low=[]
    length_dates=len(dates)

    for i in range (length_dates):
        high.append(typical_high)
        low.append(typical_low)

#Plot with axes
    plt.plot(dates, high)
    plt.plot(dates, low)
    plt.plot(matplotlib.dates.date2num(dates),levels)
    plt.plot (dates, poly(matplotlib.dates.date2num(dates)-d0))

#Added titles and labelled axes onto plots
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation = 45)
    plt.title(station.name)
    plt.show()