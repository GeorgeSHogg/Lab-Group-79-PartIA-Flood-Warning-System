from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

# rivers_by_station_number_dict =
#  
stations = build_station_list()

rivers_by_station_number(stations, N=9)