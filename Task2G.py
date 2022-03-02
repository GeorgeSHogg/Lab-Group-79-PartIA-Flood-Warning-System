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

    #Get a list of stations with levels above their normal operating range
    at_risk = stations_level_over_threshold(stations, tol)
    at_risk = [breakdown(station) for station in at_risk]

    order = 4
    future_days = 7
    min_data_threshold = 5
    min_severe = 1.7
    min_high = 1.2

    at_high_risk = []
    at_risk_rivers = []
    shortlist = []
    radius = 20

    for station in at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        if len(dates) > min_data_threshold:    
            #predicting the future water levels over the next week
            predicted = predict_max(station, dates, levels, order, future_days)
            #compairing the predicted level to predetermined benchmarks to determine the risk to the station
            if predicted > min_severe:
                #adding the river to a group of at risk rivers to use later
                if station.river not in at_risk_rivers:
                    at_risk_rivers.append(station.river)
                #finding nearby stations to use later
                for nearby_station in stations_within_radius(stations, station.coord, radius):
                    shortlist.append(nearby_station)
                #adding the town to the severe warning list 
                if station.town not in severe_towns and station.town is not None:
                    severe_towns.append(station.town)
                    appended_towns.append(station.town)
            #checking if the station should be added to the at risk group
            elif predicted > min_high:
                at_high_risk.append(station)
    

    for station in at_high_risk:
        #adding all the high risk stations' towns which are not already in the severe list to the hisk risk warning list
        if station.town not in appended_towns and station.town is not None:
            high_towns.append(station.town)
            appended_towns.append(station.town)

    for river in at_risk_rivers:
        #adding all of the stations on a river which is at risk to a shortlist
        for station in stations_by_river_return_station(stations, river):
            #if the station is not already in the shortlist add it to the shortlist
            if station not in shortlist:
                shortlist.append(station)
            #if it is in the shortlist add it's town to the high risk warning list
            else:
                if station.town not in appended_towns and station.town is not None:
                    high_towns.append(station.town)
                    appended_towns.append(station.town)

    #add the towns of all the remaining stations to the moderate warning list if they are not already in a warning list
    for station in shortlist:
        if station.town not in appended_towns and station.town is not None:
            moderate_towns.append(station.town)
            appended_towns.append(station.town)


    #add all the remaining towns to the low warning list
    for station in stations:
        if station.town not in appended_towns and station.town is not None:
            low_towns.append(station.town)
            appended_towns.append(station.town)
  
    warnings = ["Severe", "High", "Moderate", "Low"]
    towns = [severe_towns, high_towns, moderate_towns, low_towns]
    
    #print the warning lists
    for i in range(len(warnings)):
        print()
        print(warnings[i], "risk towns")
        print(*sorted(towns[i]), sep = ", ")

    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()