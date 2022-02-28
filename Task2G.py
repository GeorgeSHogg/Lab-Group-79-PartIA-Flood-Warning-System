from datetime import timedelta
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, predict_max
from floodsystem.geo import stations_within_radius
import matplotlib
import numpy as np

def breakdown(station):
    station, _ = station
    return station

def run():
    "Requirements for Task 2B"
    severe_towns = []
    high_towns = []
    moderate_towns = []
    low_towns = []

    stations = build_station_list()
    update_water_levels(stations)
    tol = 1
    at_risk = stations_level_over_threshold(stations, tol)
    at_risk = [breakdown(station) for station in at_risk]

    order = 3
    future_days = 5
    min_data_threshold = 5
    min_severe = 1.75
    min_high = 1.25

    at_severe_risk = []
    at_high_risk = []

    at_risk_rivers = []
    shortlist = []
    radius = 20

    for station in at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        if len(dates) > min_data_threshold:    
            predicted = predict_max(station, dates, levels, order, future_days)
            if predicted > min_severe:
                at_severe_risk.append(station)
                if station.river not in at_risk_rivers:
                    at_risk_rivers.append(station.rivers)
                for nearby_station in stations_within_radius(stations, station.coord, radius):
                    shortlist.append(nearby_station)
            elif predicted > min_high:
                at_high_risk.append(station)


    print("Stations at severe risk")
    print(*[station.name for station in at_severe_risk], sep = ", ")
    
    
    for station in at_severe_risk:
        
        
  
    print(*shortlist, sep = ", ")

    




if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()