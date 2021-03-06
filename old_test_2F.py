from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
import matplotlib as plt
import datetime as datetime

def test_polyfit(): 
    stations = build_station_list()
    
    list_of_5_stations_random = []
    p = 0
    for station in stations:
        list_of_5_stations_random.append(station)
        p = p + 1
        if p == 5:
            break

#degree 4 against time
    for station in list_of_5_stations_random:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days = 2))
        poly, d0 = polyfit(dates, levels, 4)
    #assert isinstance(poly, tuple) == True

