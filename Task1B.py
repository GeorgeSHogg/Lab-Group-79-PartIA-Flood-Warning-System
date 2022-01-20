from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def breakdown(station):
    """Converts a tuple of station, distance to a tuple of station.name, station.town, distance"""
    station, distance = station
    return station.name, station.town, distance

p = (52.2053, 0.1218)
stations = build_station_list()
sorted_stations = stations_by_distance(stations, p)

print("Closest 10 Stations")
print([breakdown(station) for station in sorted_stations[:10]])

print("Furthest 10 Stations")
print([breakdown(station) for station in sorted_stations[-10:]])