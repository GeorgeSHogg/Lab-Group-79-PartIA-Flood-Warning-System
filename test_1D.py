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
    assert r == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop', 'Arkle Beck']

def test_stations_by_rivers():
    s = stations_by_river
 #Test for stations on River Cam
    assert s(stations, "River Cam") == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']

test_rivers_with_stations()
test_stations_by_rivers()