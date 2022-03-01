from datetime import timedelta
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, predict_max
from floodsystem.geo import stations_within_radius, stations_by_river_return_station
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

    appended_towns = []

    stations = build_station_list()
    update_water_levels(stations)
    tol = 1
    at_risk = stations_level_over_threshold(stations, tol)
    at_risk = [breakdown(station) for station in at_risk]

    order = 4
    future_days = 5
    min_data_threshold = 5
    min_severe = 1.75
    min_high = 1.25

    at_high_risk = []
    at_risk_rivers = []
    shortlist = []
    radius = 20

    for station in at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        if len(dates) > min_data_threshold:    
            predicted = predict_max(station, dates, levels, order, future_days)
            if predicted > min_severe:
                if station.river not in at_risk_rivers:
                    at_risk_rivers.append(station.river)
                for nearby_station in stations_within_radius(stations, station.coord, radius):
                    shortlist.append(nearby_station)
                if station.town not in severe_towns:
                    severe_towns.append(station.town)
                    appended_towns.append(station.town)
            elif predicted > min_high:
                at_high_risk.append(station)
    
    for station in at_high_risk:
        if station.town not in appended_towns:
            high_towns.append(station.town)
            appended_towns.append(station.town)

    for river in at_risk_rivers:
        for station in stations_by_river_return_station(stations, river):
            if station not in shortlist:
                shortlist.append(station)
            else:
                if station.town not in appended_towns:
                    high_towns.append(station.town)
                    appended_towns.append(station.town)

    for station in shortlist:
        if station.town not in appended_towns:
            moderate_towns.append(station.town)
            appended_towns.append(station.town)


    for station in stations:
        if station not in appended_towns:
            low_towns.append(station.town)
            appended_towns.append(station.town)
  
    print()
    print(*severe_towns, sep = ", ")
    print()
    print(*high_towns, sep = ", ")
    print()
    print(*moderate_towns, sep = ", ")
    print()
    print(*low_towns, sep = ", ")
    print()


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()