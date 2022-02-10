from distutils.command.build import build
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def test_rivers_with_stations():
    #Build list of stations
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    rivers = sorted(rivers)
    r = rivers[:10]
#Test for No. of stations with at least one monitoring station
    assert len(rivers) == 950
# Test for first 10 rivers
    assert r == ['Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook',
 'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook']

def test_stations_by_rivers():
    s = stations_by_river
 #Test for stations on River Cam
    assert s(stations, "River Cam") == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Weston Bampfylde']

test_rivers_with_stations()
test_stations_by_rivers()