from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()
rivers = rivers_with_station(stations)

"""Requirements for Task 1D"""
rivers = sorted(rivers)
r = rivers[:10]
    #List of how many rivers have at least one monitoring station
   # print(rivers[:10])
print(len(rivers))
print(r)
    #Print No. of stations with at least one monitoring station
#print("First 10 - ", rivers_with_station(stations))
s = stations_by_river
print("Stations on River Aire:", s(stations, "River Aire"))
print("Stations on River Cam:", s(stations, "River Cam"))
print("Stations on River Thames:", s(stations, "River Thames"))



#def stations_by_river(stations):
 #   stations = MonitoringStation()
  #  print("Stations on River Aire: " + stations_by_river(stations, "River Aire"))
   # print("Stations on River Cam: " + stations_by_river(stations, "River Cam"))
    #print("Stations on River Thames: " + stations_by_river(stations, "River Thames"))
   # """Grouped stations by the same river

    #stations (list): list of MonitoringStation objects

    #Returns: 
    #    dictionary: maps the river as the key to a list of Monitoring objects
    #""" 
  #  stations = [MonitoringStation]
    #monitoringstations = {}

   # for station in monitoringstations:
    #    if station in monitoringstations:
     #       monitoringstations[stations].append(station.name)