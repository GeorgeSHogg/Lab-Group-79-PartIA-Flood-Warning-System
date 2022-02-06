# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from os import stat
import numpy as np


def hav(theta):
    """Finds the haversine of an angle"""
    theta = theta / 360 * 2 * np.pi
    return np.square(np.sin(theta / 2))

def archav(theta):
    """Finds the archaversine of an angle"""
    return 2 * np.arcsin(np.sqrt(theta))

def hav_formula(p1, p2):
    hav_theta = hav(p2[0] - p1[0]) + \
        (1 - hav(p2[0] - p1[0]) - hav(p2[0] + p1[0])) * hav(p2[1] - p1[1])
    return hav_theta

def distance(p1, p2):
    radius = 6371
    hav_theta = hav_formula(p1, p2)
    theta = archav(hav_theta)
    return theta * radius

def stations_by_distance(stations, p):
    """Finds the distance of all stations to a specified point and returns them as an ordered list sorted by ascending distance"""
    stations = [(station, distance(station.coord, p)) for station in stations]
    return sorted(stations, key = lambda station: station[1])

def stations_within_radius(stations, centre, r):
    station_list = []
    for station in stations:
        if distance(station.coord, centre) < r:
            station_list.append(station)
    return station_list

def rivers_with_station(stations):
    #List of how many rivers have at least one monitoring station
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations, river):
    names = []
    for station in stations:
        if station.river == river:
            names.append(station.name)
    names = sorted(names)
    return names
        
def rivers_by_station_number(stations, N):
    river = []
    river = river.append(river.name)
    station = stations_by_river
    
    return river, len(station)