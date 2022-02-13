from os import stat
import numpy as np
import operator

def stations_level_over_threshold(stations, tol):
    at_risk_stations = []
    for station in stations:
        level = station.relative_water_level()
        if level != None:
            if level >= tol:
                at_risk_stations.append((station, level))
    return sorted(at_risk_stations, key = lambda x : x[1], reverse = True)

def most_at_risk_stations(stations, N):
    at_risk_stations = []
    for station in stations:
        level = station.relative_water_level()
        if level != None:
            at_risk_stations.append((station, level))
    at_risk_stations.sort(key = lambda x : x[1], reverse = True)
    return at_risk_stations[:N]