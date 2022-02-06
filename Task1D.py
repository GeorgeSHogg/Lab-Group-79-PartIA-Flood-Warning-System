from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
"""Requirements for Task 1D"""
stations = build_station_list()
rivers = rivers_with_station(stations)
s = stations_by_river

#First 10 rivers sorted
rivers = sorted(rivers)
r = rivers[:10]

#Print No. of stations with at least one monitoring station
print(len(rivers))
#First 10 - , rivers_with_station(stations))
print(r)

#Stations on rivers Aire, Cam & Thames
print("Stations on River Aire:", s(stations, "River Aire"))
print("Stations on River Cam:", s(stations, "River Cam"))
print("Stations on River Thames:", s(stations, "River Thames"))


