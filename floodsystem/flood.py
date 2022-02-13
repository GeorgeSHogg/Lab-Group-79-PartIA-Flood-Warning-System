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