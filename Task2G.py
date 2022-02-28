from datetime import timedelta
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit

def breakdown(station):
    station, _ = station
    return station

def run():
    "Requirements for Task 2B"
    stations = build_station_list()
    update_water_levels(stations)
    tol = 1.5
    at_risk = stations_level_over_threshold(stations, tol)
    at_risk = [breakdown(station) for station in at_risk]

    order = 2
    future_days = 0
    threshold = 5
    for station in at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 2))
        if len(dates) > threshold:    
            low, high = station.typical_range
            poly, d0 = polyfit(dates, levels, order)
            predicted = poly(future_days + 3) + d0
            print(high)
            predicted_relative = (predicted - low) / (high - low)
            print(predicted_relative)




if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()