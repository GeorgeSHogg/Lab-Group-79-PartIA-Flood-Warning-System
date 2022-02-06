from floodsystem.stationdata import build_station_list

def test_typical_range_consistent():
    stations = build_station_list()
    
    station1 = stations[0]
    station1.typical_range = None

    station2 = stations[1]
    station2.typical_range = (100, 1)

    station3 = stations[2]
    station3.typical_range = (1, 100)

    assert station1.typical_range_consistent() == False
    assert station2.typical_range_consistent() == False
    assert station3.typical_range_consistent() == True

test_typical_range_consistent()