import matplotlib as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def plot_water_levels(station, dates, levels):

    station = build_station_list()

    dates = datetime()

    levels = update_water_levels()

#Plot with axes
    plt.plot(dates, levels)

#Added titles and labelled axes onto plots
    plt.xlabel("Time for a station (s)")
    plt.ylabel("Water Level (m)")
    plt.title(station)

#Display plot
    plt.tight_layout()
    plt.show()